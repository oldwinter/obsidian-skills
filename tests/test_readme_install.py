import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ReadmeInstallTests(unittest.TestCase):
    def test_npx_commands_use_full_depth_and_marketplace_once(self) -> None:
        npx_lines = [
            line.strip()
            for line in README.splitlines()
            if line.strip().startswith("npx skills add")
        ]
        self.assertGreaterEqual(len(npx_lines), 1)
        for line in npx_lines:
            self.assertIn("--full-depth", line)

        marketplace = re.findall(
            r"/plugin marketplace add oldwinter/obsidian-skills", README
        )
        install = re.findall(r"/plugin install obsidian@obsidian-skills", README)
        self.assertEqual(len(marketplace), 1, marketplace)
        self.assertEqual(len(install), 1, install)
        self.assertIn("skills/", README)
        self.assertNotIn("npx skills add git@github.com:oldwinter/obsidian-skills.git\n", README)


if __name__ == "__main__":
    unittest.main()
