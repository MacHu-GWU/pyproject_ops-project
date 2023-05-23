# -*- coding: utf-8 -*-

import dataclasses

from .pyproject_paths import PyProjectPaths
from .pyproject_venv import PyProjectVenv
from .pyproject_deps import PyProjectDeps
from .pyproject_tests import PyProjectTests
from .pyproject_docs import PyProjectDocs


@dataclasses.dataclass
class PyProjectOps(
    PyProjectPaths,
    PyProjectVenv,
    PyProjectDeps,
    PyProjectTests,
    PyProjectDocs,
):
    pass
