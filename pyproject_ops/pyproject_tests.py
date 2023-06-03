# -*- coding: utf-8 -*-

import typing as T
import subprocess
import dataclasses


if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectTests:
    def run_unit_test(self: "PyProjectOps"):
        args = [
            f"{self.path_venv_bin_pytest}",
            f"{self.dir_tests}",
            "-s",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)

    def run_cov_test(self: "PyProjectOps"):
        args = [
            f"{self.path_venv_bin_pytest}",
            "-s",
            "--tb=native",
            f"--rootdir={self.dir_project_root}",
            f"--cov={self.package_name}",
            "--cov-report",
            "term-missing",
            "--cov-report",
            f"html:{self.dir_htmlcov}",
            f"{self.dir_tests}",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)

    def run_int_test(self: "PyProjectOps"):
        args = [
            f"{self.path_venv_bin_pytest}",
            f"{self.dir_tests_int}",
            "-s",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)

    def run_load_test(self: "PyProjectOps"):
        args = [
            f"{self.path_venv_bin_pytest}",
            f"{self.dir_tests_load}",
            "-s",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)
