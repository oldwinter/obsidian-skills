import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = (ROOT / "skills" / "json-canvas" / "SKILL.md").read_text(encoding="utf-8")
EXAMPLES = (ROOT / "skills" / "json-canvas" / "references" / "EXAMPLES.md").read_text(
    encoding="utf-8"
)

DEFAULT_HEX = {
    "1": "#fb464c",
    "2": "#e9973f",
    "3": "#e0de71",
    "4": "#44cf6e",
    "5": "#53dfdd",
    "6": "#a882ff",
}
PRESETS = set(DEFAULT_HEX)


def example_colors(markdown: str) -> list[str]:
    colors: list[str] = []
    for block in re.findall(r"```json\n(.*?)```", markdown, flags=re.DOTALL):
        payload = json.loads(block)
        for item in payload.get("nodes", []) + payload.get("edges", []):
            if "color" in item:
                colors.append(str(item["color"]))
    return colors


class CanvasColorTests(unittest.TestCase):
    def test_skill_documents_obsidian_presets_without_pure_red(self) -> None:
        self.assertIsNone(
            re.search(r"#ff0000", SKILL, flags=re.IGNORECASE),
            "SKILL.md should not teach #FF0000",
        )
        for hex_value in DEFAULT_HEX.values():
            self.assertIn(hex_value, SKILL)

    def test_examples_use_preset_colors_only(self) -> None:
        colors = example_colors(EXAMPLES)
        self.assertGreater(len(colors), 0)
        for color in colors:
            self.assertIn(color, PRESETS, f"example color {color!r} is not a preset")


if __name__ == "__main__":
    unittest.main()
