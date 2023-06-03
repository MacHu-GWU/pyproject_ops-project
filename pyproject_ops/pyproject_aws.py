# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from pathlib_mate import Path


if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectAWS:
    @property
    def path_bin_aws(self: "PyProjectOps") -> Path:
        return self.get_path_dynamic_bin_cli("aws")
