---
name: defuddle
description: Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch when the user provides a URL to read or analyze, for online documentation, articles, blog posts, or any standard web page. Do NOT use for URLs ending in .md — those are already markdown, use WebFetch directly. When saving a clipped page as an Obsidian note, use --markdown --frontmatter.
---

# Defuddle

## 中文执行导读

这是 `defuddle` 的中文 runtime 入口。

中文 Obsidian 请求命中本 skill 时，先确认文件类型和目标操作，再按下方上游流程执行。输出说明使用简体中文；wikilink、embed、callout、property、filter、formula、CLI 参数、schema、路径、URL 和代码保持原样。剪藏成笔记时用 `--markdown --frontmatter`，不要只输出裸 HTML。

Use Defuddle CLI to extract clean readable content from web pages. Prefer over WebFetch for standard web pages — it removes navigation, ads, and clutter, reducing token usage.

If not installed: `npm install -g defuddle`

## Usage

Prefer `--markdown` (`--md` is an alias) for markdown output:

```bash
defuddle parse <url> --markdown
```

Save a clipped page as an Obsidian note. `--frontmatter` prepends YAML properties (`title`, `author`, `source`, and related metadata):

```bash
defuddle parse <url> --markdown --frontmatter -o content.md
```

Extract specific metadata:

```bash
defuddle parse <url> -p title
defuddle parse <url> -p description
defuddle parse <url> -p domain
```

If a site returns 403, retry with `--user-agent`.

## Output formats

| Flag | Format |
|------|--------|
| `--markdown` / `--md` | Markdown (default choice) |
| `--frontmatter` / `-f` | Prepend YAML properties to the output |
| `--json` | JSON with both HTML and markdown |
| (none) | HTML |
| `-p <name>` | Specific metadata property |
| `--user-agent` | Custom `User-Agent` for HTTP fetches |
