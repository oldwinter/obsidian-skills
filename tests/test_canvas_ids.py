import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "json-canvas" / "SKILL.md").read_text(encoding="utf-8")


class CanvasIdTests(unittest.TestCase):
    def test_skill_accepts_every_unique_string_id(self) -> None:
        self.assertIn("unique string", SKILL.lower())
        self.assertIsNone(
            re.search(r"unique 16-(?:character|char)", SKILL, flags=re.IGNORECASE)
        )
        self.assertIn("not required", SKILL.lower())


if __name__ == "__main__":
    unittest.main()
