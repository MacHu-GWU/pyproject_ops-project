# -*- coding: utf-8 -*-

import inspect
from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps


pyops = PyProjectOps(
    dir_project_root=Path.dir_here(__file__).parent,
    package_name="pyproject_ops",
    python_version="3.8",
)


class TestPyprojectPaths:
    def test(self):
        path_attributes = []
        for name, type_ in inspect.getmembers(PyProjectOps):
            if isinstance(type_, property):
                if (
                    name.startswith("dir_") or name.startswith("path_")
                ):
                    path_attributes.append(name)
        path_list = [
            getattr(pyops, name)
            for name in path_attributes
        ]
        path_list.sort()
        for path in path_list:
            print(path)


if __name__ == "__main__":
    from pyproject_ops.tests import run_cov_test

    run_cov_test(__file__, "pyproject_ops.pyproject_paths", preview=False)
