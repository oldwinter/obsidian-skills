import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "obsidian-cli" / "SKILL.md").read_text(encoding="utf-8")


class ObsidianCliContractTests(unittest.TestCase):
    def test_skill_documents_cli_prerequisites(self) -> None:
        self.assertIn("compatibility:", SKILL)
        self.assertIn("1.12.7", SKILL)
        self.assertIn("Command line interface", SKILL)
        self.assertIn("launches Obsidian", SKILL)

    def test_skill_documents_vault_resolution_order(self) -> None:
        self.assertIn("current working directory", SKILL)
        self.assertRegex(SKILL, r"current working directory.*vault.*active vault")

    def test_skill_does_not_teach_the_uri_only_silent_flag(self) -> None:
        self.assertIsNone(re.search(r"\bsilent\b", SKILL))
        self.assertIn("open` or `newtab", SKILL)


if __name__ == "__main__":
    unittest.main()
