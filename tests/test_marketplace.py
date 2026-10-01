"""Regression checks for the Bauer marketplace entry (standard library only)."""

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BauerMarketplaceTest(unittest.TestCase):
    def test_bauer_uses_canonical_github_source_and_metadata(self):
        catalog = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        entries = [plugin for plugin in catalog["plugins"] if plugin["name"] == "bauer"]
        self.assertEqual(len(entries), 1, "Bauer must appear exactly once")
        bauer = entries[0]
        expected = {
            "source": {"source": "github", "repo": "luxsolari/bauer"},
            "description": "Evidence-backed security audits with optional Jev review.",
            "author": {"name": "Lux Solari"},
            "homepage": "https://github.com/luxsolari/bauer",
            "repository": "https://github.com/luxsolari/bauer",
            "license": "MIT",
            "keywords": ["security", "owasp", "llm", "audit"],
            "category": "security",
        }
        for key, value in expected.items():
            with self.subTest(field=key):
                self.assertEqual(bauer.get(key), value)
        self.assertNotIn("version", bauer, "Resolve versions from the upstream plugin manifest")


if __name__ == "__main__":
    unittest.main()
