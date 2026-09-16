import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(
    path.name
    for path in (ROOT / "skills").iterdir()
    if path.is_dir() and (path / "SKILL.md").is_file()
)
KNAP = (ROOT / "skills" / "knap" / "SKILL.md").read_text(encoding="utf-8")


class SkillBilingualTests(unittest.TestCase):
    def test_every_skill_has_chinese_runtime_guide(self) -> None:
        for name in SKILLS:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("## 中文执行导读", text, name)
            self.assertIn(f"这是 `{name}` 的中文 runtime 入口。", text, name)

    def test_knap_uses_english_description_and_body_headings(self) -> None:
        match = re.search(r"^description:\s*(.+)$", KNAP, flags=re.MULTILINE)
        self.assertIsNotNone(match)
        self.assertTrue(
            match.group(1).startswith("Render Markdown"),
            match.group(1),
        )
        for heading in ("## Usage", "## Templates", "## Defuddle pipeline", "## Batch rendering"):
            self.assertIn(heading, KNAP)
        for heading in ("## 用法", "## 模板", "## Defuddle 流程", "## 批量渲染"):
            self.assertNotIn(heading, KNAP)


if __name__ == "__main__":
    unittest.main()
