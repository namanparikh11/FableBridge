from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


render = load_script("fablebridge_render", ROOT / "scripts" / "render.py")
installer = load_script("fablebridge_install", ROOT / "scripts" / "install.py")


class FableBridgeTests(unittest.TestCase):
    def test_all_committed_adapters_match_renderer(self):
        for name, path in render.TARGETS.items():
            self.assertTrue(path.is_file(), name)
            self.assertEqual(path.read_text(encoding="utf-8"), render.render(name), name)

    def test_installer_copies_codex_adapter(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            destination = installer.install("codex", target)
            self.assertEqual(destination, target.resolve() / "AGENTS.md")
            self.assertEqual(
                destination.read_text(encoding="utf-8"),
                (ROOT / "adapters" / "codex" / "AGENTS.md").read_text(encoding="utf-8"),
            )

    def test_installer_refuses_silent_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            existing = target / "CLAUDE.md"
            existing.write_text("project-specific rules\n", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                installer.install("claude-code", target)
            self.assertEqual(existing.read_text(encoding="utf-8"), "project-specific rules\n")

    def test_cursor_install_creates_native_rule_path(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            destination = installer.install("cursor", target)
            self.assertEqual(destination, target.resolve() / ".cursor" / "rules" / "fable51.mdc")
            self.assertTrue(destination.is_file())


if __name__ == "__main__":
    unittest.main()
