from tempfile import TemporaryDirectory

from src.result import Error, Result, Success
from src.test_case import TestCaseBase


class TestCase(TestCaseBase):
    @property
    def test_target(self) -> str:
        return "//:unused_public_dep"

    def execute_test_logic(self) -> Result:
        with TemporaryDirectory() as output_base:
            self._create_reports(startup_args=[f"--output_base={output_base}"])
            self._run_automatic_fix(extra_args=[f"--bazel-bin={output_base}"])

            target_deps = self._get_target_attribute(target=self.test_target, attribute="deps")
            if target_deps == {"//:lib_a"}:
                return Success()
            else:
                return Error(f"Dependencies have not been adapted correctly. Unexpected dependencies: {target_deps}")
