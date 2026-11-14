"""Guard the free research connection and its continuation link."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import package


class PackageTests(unittest.TestCase):
    def test_current_package_validates(self):
        package.validate()

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
