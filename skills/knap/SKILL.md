---
name: knap
description: 使用 Knap CLI 从模板和结构化数据渲染 Markdown。用户要求应用 Knap 模板、将 JSON 或 CSV 转成笔记、批量生成 Markdown 文件，或把 Defuddle 输出格式化成笔记时使用。
---

# Knap

使用 Knap CLI 通过变量、filters 和逻辑渲染 Markdown 模板。

如果尚未安装：`npm install -g knap`（需要 Node.js 20 或更高版本）。也可以使用 `npx knap`。

运行 `knap --help` 查看可用命令和选项。通过 CLI 的离线参考了解模板语言：

```bash
knap help syntax
knap help filters
knap help filter date
knap help tags
knap help tag for
```

先从列表中找到名称，再针对具体项目请求语法、参数和预期输出示例。

## 用法

使用 JSON 变量渲染模板：

```bash
knap render template.md --data article.json -o note.md
```

内联提供模板和数据：

```bash
knap render -t '# {{ title | trim }}' --data-json '{"title":"Hello"}'
```

覆盖变量，或通过管道传入 JSON 数据：

```bash
knap render template.md --data article.json --set 'title=Custom title'
cat article.json | knap render template.md --data -
```

数据必须是 JSON object，其属性会成为模板变量。`--set` 用字符串覆盖顶层字面量 key。嵌套对象、数组、数字和布尔值应使用 JSON 表示。

选择一种模板来源（文件、`-t` 或 stdin）和一种数据来源（`--data` 或 `--data-json`）。只有一个输入可以读取 stdin。如果没有模板文件或 `-t`，Knap 会从 stdin 读取模板。

默认输出到 stdout。`-o` 会创建父目录，并在渲染成功后覆盖目标文件。错误以状态码 `1` 退出，诊断信息写入 stderr。成功输出也可能伴随 warning。

## 模板

使用 `{{ variable }}` 输出值，使用 `|` 调用 filter，使用 `{% ... %}` 表达逻辑。例如，将下面内容保存为 `template.md`：

```knap
---
{{ title | yaml_property:"title" }}
{{ tags | yaml_property:"tags" }}
---
# {{ title | trim }}
{% if author %}
By {{ author }}
{% endif %}

{{ content }}
```

完整的 frontmatter property 使用 `yaml_property`，以确保值被正确引用和缩进。CLI 包含标准 filters，但不提供 Web Clipper 浏览器变量、selectors、prompts 或依赖 DOM 的 HTML filters。请通过 JSON 提供变量。

渲染前检查模板：

```bash
knap validate template.md
```

验证会在没有数据或文件输出的情况下检查语法、filter 名称和静态 filter 参数。它不会检查变量是否存在、runtime 值或动态参数；请使用真实数据渲染来检查 runtime 行为。诊断信息写入 stderr，并包含相关帮助命令。

## Defuddle 流程

先将网页提取为包含 Markdown 内容的 JSON，再渲染成笔记：

```bash
defuddle parse https://example.com/article --md --json \
  | knap render template.md --data - -o note.md
```

Defuddle 的 JSON properties（例如 `title` 和 `content`）会直接成为模板变量。

## 批量渲染

为每一行 CSV、JSON array object 或目录中的每个 JSON 文件生成一个文件：

```bash
knap batch template.md --data articles.csv --output-dir notes \
  --filename '{{ title | safe_name }}.md'
```

数组使用 `--data articles.json`，JSON object 目录使用 `--data ./articles`。CSV headers 会成为变量名，值保持为字符串。管道数据默认按 JSON 处理，管道输入 CSV 时添加 `--format csv`。

使用 `--dry-run` 可以只验证并列出输出路径而不写文件。已有文件需要 `--overwrite`，dry run 期间也一样。即使使用 `--overwrite`，批处理中出现重复输出文件名仍会报错。

Filename 模板必须生成带扩展名的单个文件名，不能包含目录。数据生成的名称使用 `safe_name`。如果没有 `--filename`，Knap 会保留源 JSON basename，或把 CSV 行和数组元素编号为 `1.md`、`2.md` 等文件名。
