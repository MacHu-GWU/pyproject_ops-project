# -*- coding: utf-8 -*-

from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps

pyops = PyProjectOps(
    dir_project_root=Path.dir_here(__file__),
    package_name="pyproject_ops",
    python_version="3.8",
)

pyops.remove_virtualenv()
pyops.create_virtualenv()
pyops.pip_install_all()
pyops.run_cov_test()
