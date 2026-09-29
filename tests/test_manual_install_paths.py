import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ManualInstallPathTests(unittest.TestCase):
    def test_claude_path_is_vault_local(self) -> None:
        self.assertNotIn("`/.claude`", README)
        self.assertIn("<vault>/.claude/skills/<skill-name>/SKILL.md", README)

    def test_codex_copy_has_no_extra_skills_wrapper(self) -> None:
        self.assertIn("cp -R skills/. ~/.codex/skills/", README)
        self.assertIn("~/.codex/skills/<skill-name>/SKILL.md", README)


if __name__ == "__main__":
    unittest.main()
