import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = (ROOT / ".github" / "workflows" / "tests.yml").read_text(encoding="utf-8")


class WorkflowHardeningTests(unittest.TestCase):
    def test_actions_are_pinned_to_full_commit_shas(self) -> None:
        for action in ("actions/checkout", "actions/setup-python"):
            self.assertRegex(WORKFLOW, rf"uses: {action}@[0-9a-f]{{40}}\s+# v\d+")

    def test_workflow_grants_only_read_access_to_contents(self) -> None:
        self.assertRegex(WORKFLOW, r"permissions:\n  contents: read")

    def test_job_has_a_timeout(self) -> None:
        self.assertRegex(WORKFLOW, r"test:\n    timeout-minutes: \d+")

    def test_obsolete_runs_are_cancelled(self) -> None:
        self.assertIn("concurrency:", WORKFLOW)
        self.assertIn("group: ${{ github.workflow }}-${{ github.ref }}", WORKFLOW)
        self.assertIn("cancel-in-progress: true", WORKFLOW)


if __name__ == "__main__":
    unittest.main()
