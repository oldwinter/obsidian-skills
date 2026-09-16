import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = (ROOT / "docs" / "translation-profile.zh-CN.md").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")
SKILLS = sorted(
    path.name
    for path in (ROOT / "skills").iterdir()
    if path.is_dir() and (path / "SKILL.md").is_file()
)


class SkillInventoryTests(unittest.TestCase):
    def test_docs_name_every_skill_and_lock_count(self) -> None:
        self.assertGreaterEqual(len(SKILLS), 1)
        for name in SKILLS:
            self.assertIn(name, PROFILE, f"{name} missing from translation profile")
            self.assertIn(
                f"[{name}](skills/{name})",
                README,
                f"{name} missing from README skill table",
            )

        count = re.search(r"当前 (\d+) 个：", PROFILE)
        self.assertIsNotNone(count, "translation profile must state the live skill count")
        self.assertEqual(int(count.group(1)), len(SKILLS))

        table_names = re.findall(
            r"^\| \[([^\]]+)\]\(skills/\1\)", README, flags=re.MULTILINE
        )
        self.assertEqual(sorted(table_names), SKILLS)

        stale = re.compile(r"5 个(?: runtime)? skill")
        self.assertIsNone(stale.search(PROFILE), PROFILE)
        self.assertIsNone(stale.search(README), README)


if __name__ == "__main__":
    unittest.main()
