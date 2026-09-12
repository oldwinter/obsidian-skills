# Obsidian Skills 中文化档案

同步上游后先读本档案，再处理新增或变更内容。

## 项目定位

- 上游项目：`kepano/obsidian-skills`
- 中文 fork：`oldwinter/obsidian-skills`
- 当前同步上游 commit：`8ccef29ae8624eccc734e77ced4a6e54baf5d83a`
- 主要安装面：Claude Code/Codex plugin marketplace、skills CLI、直接 clone
- 中文 runtime 入口：6 个 `skills/*/SKILL.md`

## 中文化目标

让中文用户可以直接使用 Obsidian Flavored Markdown、Bases、JSON Canvas、Obsidian CLI、Defuddle 和 Knap skill。wikilink、embed、callout、property、filter、formula、CLI 参数、JSON Canvas schema、URL 和文件扩展名保持原样；每个 runtime 入口的中文导读与技术正文共同生效。

## 安装与交付

```text
/plugin marketplace add oldwinter/obsidian-skills
/plugin install obsidian@obsidian-skills
```

或运行：

```bash
npx skills add oldwinter/obsidian-skills --full-depth
```

安装后 runtime 实际读取中文 fork 的 `skills/*/SKILL.md`。

## 同步后检查

- `git diff --check`
- `rg -n '^(<<<<<<<|=======|>>>>>>>)$' .`
- Claude marketplace/plugin JSON 校验
- 5 个 runtime skill 的 frontmatter、内部 references 和 schema 示例保持可解析
