# -*- coding: utf-8 -*-

"""
This script extract the doc string of all path property method, and generate
the documentation for README.rst.
"""

import typing as T
import inspect
from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps

pyops = PyProjectOps(
    dir_project_root=Path.dir_here(__file__).parent,
    package_name="pyproject_ops",
    python_version="3.8",
)

path_attributes = []
for name, type_ in inspect.getmembers(PyProjectOps):
    if isinstance(type_, property):
        if name.startswith("dir_") or name.startswith("path_"):
            path_attributes.append(name)

name_and_path_and_docstr_list: T.List[T.Tuple[str, Path, str]] = list()

for name in path_attributes:
    path = getattr(pyops, name)
    try:
        docstr = getattr(PyProjectOps, name).__doc__.strip().split("\n")[0]
    except:
        docstr = "no docstr"
    name_and_path_and_docstr_list.append((name, path, docstr))

name_and_path_and_docstr_list = list(
    sorted(
        name_and_path_and_docstr_list,
        key=lambda x: x[1],
    )
)

for name, path, docstr in name_and_path_and_docstr_list:
    try:
        relpath = path.relative_to(pyops.dir_project_root)
        print(f"- ``{relpath}``: ``PyProjectOps.{name}``, {docstr}")
    except ValueError:
        pass
