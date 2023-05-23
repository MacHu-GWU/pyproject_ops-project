# -*- coding: utf-8 -*-

import sys
from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps

pyops = PyProjectOps(
    dir_project_root=Path.dir_here(__file__),
    package_name="pyproject_ops",
    python_version=f"{sys.version_info.major}.{sys.version_info.minor}",
)

pyops.remove_virtualenv()
pyops.create_virtualenv()
pyops.pip_install_all()
pyops.run_cov_test()
