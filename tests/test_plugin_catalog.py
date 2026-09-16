import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
MARKET = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
SKILLS = sorted(
    path.name
    for path in (ROOT / "skills").iterdir()
    if path.is_dir() and (path / "SKILL.md").is_file()
)


def catalog_text(payload: dict) -> str:
    parts = [str(payload.get("description", ""))]
    parts.extend(str(item) for item in payload.get("keywords", []))
    for plugin in payload.get("plugins", []):
        parts.append(str(plugin.get("description", "")))
        parts.extend(str(item) for item in plugin.get("keywords", []))
    return " ".join(parts).lower()


class PluginCatalogTests(unittest.TestCase):
    def test_every_skill_is_named_in_plugin_and_marketplace(self) -> None:
        self.assertGreaterEqual(len(SKILLS), 1)
        plugin_text = catalog_text(PLUGIN)
        market_text = catalog_text(MARKET)
        for name in SKILLS:
            self.assertIn(name, plugin_text, f"{name} missing from plugin.json")
            self.assertIn(name, market_text, f"{name} missing from marketplace.json")

    def test_plugin_and_marketplace_plugin_versions_match(self) -> None:
        self.assertEqual(PLUGIN["version"], MARKET["plugins"][0]["version"])


if __name__ == "__main__":
    unittest.main()
