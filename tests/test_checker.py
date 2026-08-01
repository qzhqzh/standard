from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from repo_standard.checker import scan_repository
from repo_standard.models import Level, Policy, Rule
from repo_standard.policy import PolicyError, load_policy


class CheckerTests(unittest.TestCase):
    def test_any_and_all_rules(self) -> None:
        policy = Policy(
            schema_version=1,
            name="test",
            rules=(
                Rule(
                    id="readme",
                    title="README",
                    level=Level.REQUIRED,
                    mode="any",
                    paths=("README.md", "README.rst"),
                    rationale="identity",
                    remediation="add readme",
                ),
                Rule(
                    id="text-baseline",
                    title="Text baseline",
                    level=Level.RECOMMENDED,
                    mode="all",
                    paths=(".editorconfig", ".gitattributes"),
                    rationale="consistent text",
                    remediation="add files",
                ),
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("# demo\n", encoding="utf-8")
            (root / ".editorconfig").write_text("root = true\n", encoding="utf-8")
            report = scan_repository(root, policy)

        self.assertTrue(report.results[0].passed)
        self.assertFalse(report.results[1].passed)
        self.assertEqual(report.counts()["required"], {"passed": 1, "total": 1})
        self.assertLess(report.score, 100)

    def test_glob_rule(self) -> None:
        policy = Policy(
            schema_version=1,
            name="test",
            rules=(
                Rule(
                    id="workflow",
                    title="Workflow",
                    level=Level.REQUIRED,
                    mode="any",
                    paths=(".github/workflows/*.yml",),
                    rationale="automation",
                    remediation="add workflow",
                ),
            ),
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            workflow = root / ".github" / "workflows"
            workflow.mkdir(parents=True)
            (workflow / "ci.yml").write_text("name: CI\n", encoding="utf-8")
            report = scan_repository(root, policy)

        self.assertTrue(report.results[0].passed)
        self.assertEqual(report.results[0].matched_paths, (".github/workflows/ci.yml",))

    def test_policy_rejects_parent_traversal(self) -> None:
        unsafe = (
            'schema_version = 1\nname = "unsafe"\n\n[[rules]]\n'
            'id = "x"\ntitle = "x"\nlevel = "required"\nmode = "any"\n'
            'paths = ["../secret"]\nrationale = "x"\nremediation = "x"\n'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "policy.toml"
            path.write_text(unsafe, encoding="utf-8")
            with self.assertRaises(PolicyError):
                load_policy(path)

    def test_root_policy_matches_packaged_policy(self) -> None:
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(
            (root / "standard.toml").read_text(encoding="utf-8"),
            (root / "src/repo_standard/default_policy.toml").read_text(encoding="utf-8"),
        )


if __name__ == "__main__":
    unittest.main()
