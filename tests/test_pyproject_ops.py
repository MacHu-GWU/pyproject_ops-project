# -*- coding: utf-8 -*-

from pathlib_mate import Path
from pyproject_ops.api import PyProjectOps


p = PyProjectOps(
    dir_project_root=Path.dir_here(__file__).parent,
    package_name="pyproject_ops",
    python_version="3.8",
)


class TestPyprojectPaths:
    def test(self):
        _ = p.dir_venv
        _ = p.dir_venv_bin
        _ = p.path_venv_bin_python
        _ = p.path_venv_bin_pip
        _ = p.path_venv_bin_pytest
        _ = p.path_bin_poetry
        _ = p.path_bin_twine
        _ = p.dir_tests
        _ = p.dir_htmlcov
        _ = p.dir_sphinx_doc
        _ = p.dir_sphinx_doc_source
        _ = p.dir_sphinx_doc_source_conf_py
        _ = p.dir_sphinx_doc_source_python_lib
        _ = p.dir_sphinx_doc_build
        _ = p.dir_sphinx_doc_build_html
        _ = p.path_requirements_main
        _ = p.path_requirements_dev
        _ = p.path_requirements_test
        _ = p.path_requirements_doc
        _ = p.path_requirements_automation
        _ = p.path_poetry_lock
        _ = p.path_poetry_lock_hash_json
        _ = p.path_pyproject_toml
        _ = p.dir_build
        _ = p.dir_dist
        _ = p.dir_build_lambda
        _ = p.dir_build_lambda_python
        _ = p.path_build_lambda_bin_aws
        _ = p.path_build_lambda_source_zip
        _ = p.path_build_lambda_layer_zip
        _ = p.dir_lambda_app
        _ = p.path_chalice_config
        _ = p.dir_lambda_app_vendor
        _ = p.dir_lambda_app_deployed
        _ = p.path_lambda_update_chalice_config_script
        _ = p.path_lambda_app_py
        _ = p.dir_home
        _ = p.dir_config
        _ = p.path_config_json
        _ = p.path_secret_config_json


class PyProjectVenv:
    def test(self):
        _ = p.create_virtualenv
        _ = p.remove_virtualenv


class PyProjectDeps:
    def test(self):
        _ = p.poetry_lock
        _ = p.poetry_install
        _ = p.poetry_install_dev
        _ = p.poetry_install_test
        _ = p.poetry_install_doc
        _ = p.poetry_install_all
        _ = p._do_we_need_poetry_export
        _ = p._poetry_export_group
        _ = p._poetry_export
        _ = p.poetry_export
        _ = p._try_poetry_export
        _ = p.pip_install
        _ = p.pip_install_dev
        _ = p.pip_install_test
        _ = p.pip_install_doc
        _ = p.pip_install_automation
        _ = p.pip_install_all


class PyProjectTests:
    def test(self):
        _ = p.run_unit_test
        _ = p.run_cov_test


class PyProjectDocs:
    def test(self):
        _ = p.build_doc
        _ = p.view_doc
        _ = p.deploy_versioned_doc
        _ = p.deploy_latest_doc
        _ = p.view_latest_doc


if __name__ == "__main__":
    from pyproject_ops.tests import run_cov_test

    run_cov_test(__file__, "pyproject_ops", preview=False)
