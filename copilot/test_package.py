"""Guard the free research connection and its continuation link."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import package
from PIL import Image


class PackageTests(unittest.TestCase):
    def test_current_package_validates(self):
        package.validate()

    def test_store_description_explains_setup_and_limits(self):
        manifest = json.loads((package.ROOT / "manifest.json").read_text())
        short = manifest["description"]["short"]
        full = manifest["description"]["full"]
        self.assertLessEqual(len(short), 80)
        self.assertIn("Microsoft 365 Copilot", short)
        self.assertIn("agents for Microsoft Copilot", full)
        for required in ["https://www.arca.inc/mcp", "https://www.arca.inc/support", "English", "no Arca account", "public records only", "outside Teams"]:
            self.assertIn(required, full)

    def test_function_descriptions_are_complete_sentences(self):
        plugin = json.loads((package.ROOT / "ai-plugin.json").read_text())
        for function in plugin["functions"]:
            with self.subTest(function=function["name"]):
                self.assertLessEqual(len(function["description"]), 1024)
                self.assertTrue(function["description"].endswith((".", "!", "?")))

    def test_agent_requests_clickable_sources_not_bare_urls(self):
        agent = json.loads((package.ROOT / "declarativeAgent.json").read_text())
        self.assertIn("clickable Markdown link", agent["instructions"])
        self.assertIn("[label](URL)", agent["instructions"])

    def test_outline_icon_is_white_with_transparent_background(self):
        with Image.open(package.ROOT / "outline.png") as image:
            self.assertEqual(image.size, (32, 32))
            rgba = image.convert("RGBA")
            pixels = [rgba.getpixel((x, y)) for y in range(rgba.height) for x in range(rgba.width)]
            self.assertTrue(any(alpha == 0 for _, _, _, alpha in pixels))
            self.assertTrue(any(alpha > 0 for _, _, _, alpha in pixels))
            self.assertTrue(all((r, g, b) == (255, 255, 255) for r, g, b, alpha in pixels if alpha > 0))

    def test_missing_continuation_instruction_fails_validation(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for name in package.FILES:
                (root / name).write_bytes((package.ROOT / name).read_bytes())
            path = root / "declarativeAgent.json"
            agent = json.loads(path.read_text())
            agent["instructions"] = "Search public research and cite the original sources."
            path.write_text(json.dumps(agent))
            with patch.object(package, "ROOT", root), self.assertRaises(AssertionError):
                package.validate()


if __name__ == "__main__":
    unittest.main()
