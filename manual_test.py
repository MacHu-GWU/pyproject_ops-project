# -*- coding: utf-8 -*-

from pathlib import Path
from pyproject_ops.api import PyProjectOps

py_ops = PyProjectOps(
    dir_project_root=Path(__file__).absolute().parent,
    package_name="pyproject_ops",
    python_version="3.8",
)

# py_ops.create_virtualenv(verbose=True)
# py_ops.remove_virtualenv(verbose=True)
# py_ops.pip_install(verbose=True)
# py_ops.pip_install_dev(verbose=True)
# py_ops.pip_install_test(verbose=True)
# py_ops.pip_install_doc(verbose=True)
# py_ops.pip_install_automation(verbose=True)
# py_ops.pip_install_all(verbose=True)
# py_ops.pip_install_awsglue(verbose=True)
# py_ops.poetry_lock(verbose=True)
# py_ops.poetry_export(verbose=True)
# py_ops.poetry_install(verbose=True)
# py_ops.poetry_install_dev(verbose=True)
# py_ops.poetry_install_test(verbose=True)
# py_ops.poetry_install_doc(verbose=True)
# py_ops.poetry_install_all(verbose=True)
# py_ops.run_unit_test(verbose=True)
# py_ops.run_cov_test(verbose=True)
# py_ops.run_int_test(verbose=True)
py_ops.run_load_test(verbose=True)
# py_ops.python_build(verbose=True)
# py_ops.poetry_build(verbose=True)
# py_ops.build_doc(verbose=True)
# py_ops.view_doc(verbose=True)
# py_ops.deploy_versioned_doc(bucket="bmt-app-devops-us-east-1-doc-host", aws_profile="bmt_app_devops_us_east_1", verbose=True)
# py_ops.deploy_latest_doc(bucket="bmt-app-devops-us-east-1-doc-host", aws_profile="bmt_app_devops_us_east_1", verbose=True)

