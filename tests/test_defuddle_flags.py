import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFUDDLE = (ROOT / "skills" / "defuddle" / "SKILL.md").read_text(encoding="utf-8")
KNAP = (ROOT / "skills" / "knap" / "SKILL.md").read_text(encoding="utf-8")


class DefuddleFlagTests(unittest.TestCase):
    def test_skill_teaches_canonical_markdown_and_frontmatter(self) -> None:
        self.assertIn("--markdown", DEFUDDLE)
        self.assertIn("--frontmatter", DEFUDDLE)
        self.assertIn("--user-agent", DEFUDDLE)
        self.assertIn("defuddle parse <url> --markdown --frontmatter", DEFUDDLE)

    def test_knap_pipeline_uses_canonical_defuddle_markdown(self) -> None:
        self.assertIn("--markdown --json", KNAP)
        self.assertNotIn("--md --json", KNAP)


if __name__ == "__main__":
    unittest.main()
