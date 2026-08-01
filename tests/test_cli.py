from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from repo_standard.cli import main


class CliTests(unittest.TestCase):
    def test_json_output_and_failure_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                code = main(["check", directory, "--format", "json"])

        payload = json.loads(stdout.getvalue())
        self.assertEqual(code, 2)
        self.assertEqual(payload["schema_version"], 1)
        self.assertLess(payload["score"], 100)

    def test_never_fail_mode(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                code = main(["check", directory, "--fail-level", "never"])
        self.assertEqual(code, 0)
        self.assertIn("Repo Standard report", stdout.getvalue())

    def test_nonexistent_path_is_operational_error(self) -> None:
        path = Path("/path/that/does/not/exist/repo-standard")
        self.assertEqual(main(["check", str(path)]), 1)


if __name__ == "__main__":
    unittest.main()
