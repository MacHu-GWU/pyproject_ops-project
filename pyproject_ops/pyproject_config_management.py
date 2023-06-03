# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from pathlib_mate import Path


if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectConfigManagement:
    @property
    def dir_config(self: "PyProjectOps") -> Path:
        """
        Example: ``${dir_project_root}/config``
        """
        return self.dir_project_root.joinpath("config")

    @property
    def path_config_json(self) -> Path:
        """
        Example: ``${dir_project_root}/config/config.json``
        """
        return self.dir_config.joinpath("config.json")

    @property
    def path_secret_config_json(self: "PyProjectOps") -> Path:
        """
        Example: ``${HOME}/.projects/${package_name}/config-secret.json``
        """
        return self.dir_home.joinpath(
            ".projects", self.package_name, "config-secret.json"
        )
