# -*- coding: utf-8 -*-

import typing as T
import shutil
import subprocess
import dataclasses


if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectBuild:
    def python_build(self: "PyProjectOps"):
        if self.dir_dist.exists():
            shutil.rmtree(self.dir_dist, ignore_errors=True)
        args = [
            f"{self.path_venv_bin_python}",
            "-m",
            "build",
            "--sdist",
            "--wheel",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)

    def poetry_build(self: "PyProjectOps"):
        """

        :return:
        """
        if self.dir_dist.exists():
            shutil.rmtree(self.dir_dist, ignore_errors=True)
        args = [
            f"{self.path_bin_poetry}",
            "build",
        ]
        with self.dir_project_root.temp_cwd():
            subprocess.run(args, check=True)
