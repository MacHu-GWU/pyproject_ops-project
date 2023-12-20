# -*- coding: utf-8 -*-

import pytest
import os
import sys
from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps


@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python3.8 or higher")
def test():
    pyops = PyProjectOps(
        dir_project_root=Path.dir_here(__file__).parent,
        package_name="pyproject_ops",
        python_version=f"{sys.version_info.major}.{sys.version_info.minor}",
    )

    pyops.remove_virtualenv()
    pyops.create_virtualenv()
    pyops.pip_install_all()
    pyops.run_cov_test()
    pyops.build_doc()
    pyops.python_build()


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
