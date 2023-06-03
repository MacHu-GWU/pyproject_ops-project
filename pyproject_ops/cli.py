# -*- coding: utf-8 -*-

import typing as T
import json
import dataclasses

import fire
from pathlib_mate import Path

from .vendor.jsonutils import json_loads
from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectOpsConfig:
    package_name: str = dataclasses.field()
    dev_py_ver_major: int = dataclasses.field()
    dev_py_ver_minor: int = dataclasses.field()
    dev_py_ver_micro: int = dataclasses.field()
    doc_host_aws_profile: T.Optional[str] = dataclasses.field(default=None)
    doc_host_s3_bucket: T.Optional[str] = dataclasses.field(default=None)


def find_pyproject_ops_json(dir_cwd: Path) -> Path:
    if dir_cwd.parent == dir_cwd:
        raise FileNotFoundError(
            f"Cannot find 'pyproject_ops.json' in {dir_cwd} or its parent directory."
        )
    path = dir_cwd.joinpath("pyproject_ops.json")
    if path.exists():
        return path
    else:
        return find_pyproject_ops_json(dir_cwd.parent)


dir_cwd = Path.cwd()
path_pyproject_ops_json = find_pyproject_ops_json(dir_cwd)
pyops_config = PyProjectOpsConfig(
    **json_loads(path_pyproject_ops_json.read_text(encoding="utf-8"))
)
pyops = PyProjectOps(
    dir_project_root=path_pyproject_ops_json.parent,
    package_name=pyops_config.package_name,
    python_version=f"{pyops_config.dev_py_ver_major}.{pyops_config.dev_py_ver_minor}",
)


class Command:
    def venv_create(self):
        """
        ** Create Virtual Environment
        """
        pyops.create_virtualenv()

    def venv_remove(self):
        """
        ** Remove Virtual Environment
        """
        pyops.remove_virtualenv()


def main():
    fire.Fire(Command)
