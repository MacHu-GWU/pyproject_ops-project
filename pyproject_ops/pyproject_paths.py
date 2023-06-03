# -*- coding: utf-8 -*-

"""
Enumeration of important paths on local file system.
"""

import typing as T
import sys
import subprocess
import dataclasses
from pathlib_mate import Path

from .compat import cached_property

if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectPaths:
    dir_project_root: Path = dataclasses.field()
    package_name: str = dataclasses.field()

    @cached_property
    def dir_home(self) -> Path:
        """
        The user home directory.

        Example: ``${HOME}``
        """
        return Path.home()

    # --------------------------------------------------------------------------
    # Virtualenv
    # --------------------------------------------------------------------------
    _VENV_RELATED = None

    @property
    def dir_venv(self) -> Path:
        """
        The virtualenv directory.

        Example: ``${dir_project_root}/.venv``
        """
        return self.dir_project_root.joinpath(".venv")

    @property
    def dir_venv_bin(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin``
        """
        return self.dir_venv.joinpath("bin")

    def get_path_venv_bin_cli(self, cmd: str) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/${cmd}``
        """
        return self.dir_venv_bin.joinpath(cmd)

    @property
    def path_venv_bin_python(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/python``
        """
        return self.get_path_venv_bin_cli("python")

    @property
    def path_venv_bin_pip(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/pip``
        """
        return self.get_path_venv_bin_cli("pip")

    @property
    def path_venv_bin_pytest(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/pytest``
        """
        return self.get_path_venv_bin_cli("pytest")

    @property
    def path_sys_executable(self) -> Path:
        return Path(sys.executable)

    def get_path_dynamic_bin_cli(self, cmd: str) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/${cmd}`` or ``${global_python_bin}/${cmd}``
        """
        p = self.dir_venv_bin.joinpath(cmd)
        if p.exists():
            return p
        p = self.path_sys_executable.parent.joinpath(cmd)
        if p.exists():
            return p
        return Path(cmd)

    @property
    def path_bin_virtualenv(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/virtualenv``
        """
        return self.get_path_dynamic_bin_cli("virtualenv")

    @property
    def path_bin_poetry(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/poetry``
        """
        return self.get_path_dynamic_bin_cli("poetry")

    @property
    def path_bin_twine(self) -> Path:
        """
        Example: ``${dir_project_root}/.venv/bin/twine``
        """
        return self.get_path_dynamic_bin_cli("twine")

    # --------------------------------------------------------------------------
    # Source code
    # --------------------------------------------------------------------------
    @property
    def dir_python_lib(self) -> Path:
        """
        Example: ``${dir_project_root}/${package_name}``
        """
        return self.dir_project_root.joinpath(self.package_name)

    @property
    def path_version_py(self) -> Path:
        """
        Example: ``${dir_project_root}/${package_name}/_version.py``
        """
        return self.dir_python_lib.joinpath("_version.py")

    @cached_property
    def package_version(self) -> str:
        args = ["python", f"{self.path_version_py}"]
        res = subprocess.run(args, check=True, capture_output=True)
        return res.stdout.decode("utf-8").strip()

    # --------------------------------------------------------------------------
    # Pytest
    # --------------------------------------------------------------------------
    _PYTEST_RELATED = None

    @property
    def dir_tests(self) -> Path:
        """
        Unit test folder.

        Example: ``${dir_project_root}/tests``
        """
        return self.dir_project_root.joinpath("tests")

    @property
    def dir_tests_int(self) -> Path:
        """
        Integration test folder.

        Example: ``${dir_project_root}/tests_int``
        """
        return self.dir_project_root.joinpath("tests_int")

    @property
    def dir_tests_load(self) -> Path:
        """
        Load test folder.

        Example: ``${dir_project_root}/tests_load``
        """
        return self.dir_project_root.joinpath("tests_load")

    @property
    def dir_htmlcov(self) -> Path:
        """
        Example: ``${dir_project_root}/htmlcov``
        """
        return self.dir_project_root.joinpath("htmlcov")

    # --------------------------------------------------------------------------
    # Sphinx doc
    # --------------------------------------------------------------------------
    _SPHINX_DOC_RELATED = None

    @property
    def dir_sphinx_doc(self) -> Path:
        """
        Example: ``${dir_project_root}/docs``
        """
        return self.dir_project_root.joinpath("docs")

    @property
    def dir_sphinx_doc_source(self) -> Path:
        """
        Example: ``${dir_project_root}/docs/source``
        """
        return self.dir_sphinx_doc.joinpath("source")

    @property
    def dir_sphinx_doc_source_conf_py(self) -> Path:
        """
        Example: ``${dir_project_root}/docs/source/conf.py``
        """
        return self.dir_sphinx_doc_source.joinpath("conf.py")

    @property
    def dir_sphinx_doc_source_python_lib(self) -> Path:
        """
        Example: ``${dir_project_root}/docs/source/${package_name}``
        """
        return self.dir_sphinx_doc_source.joinpath(self.package_name)

    @property
    def dir_sphinx_doc_build(self) -> Path:
        """
        Example: ``${dir_project_root}/docs/build
        """
        return self.dir_sphinx_doc.joinpath("build")

    @property
    def dir_sphinx_doc_build_html(self) -> Path:
        """
        Example: ``${dir_project_root}/docs/build/html
        """
        return self.dir_sphinx_doc_build.joinpath("html")

    @property
    def path_sphinx_doc_build_index_html(self) -> Path:  # pragma: no cover
        """
        Example: ``${dir_project_root}/docs/build/html/index.html or README.html
        """
        if self.dir_sphinx_doc_source.joinpath("index.rst").exists():
            return self.dir_sphinx_doc_build_html.joinpath("index.html")

        if self.dir_sphinx_doc_source.joinpath("README.rst").exists():
            return self.dir_sphinx_doc_build_html.joinpath("README.html")

        raise FileNotFoundError(
            str(self.dir_sphinx_doc_build_html.joinpath("index.html"))
        )

    # --------------------------------------------------------------------------
    # Poetry
    # --------------------------------------------------------------------------
    _POETRY_RELATED = None

    @property
    def path_requirements(self) -> Path:
        """
        Example: ``${dir_project_root}/requirements.txt``
        """
        return self.dir_project_root.joinpath("requirements.txt")

    @property
    def path_requirements_dev(self) -> Path:
        """
        Example: ``${dir_project_root}/requirements-dev.txt``
        """
        return self.dir_project_root.joinpath("requirements-dev.txt")

    @property
    def path_requirements_test(self) -> Path:
        """
        Example: ``${dir_project_root}/requirements-test.txt``
        """
        return self.dir_project_root.joinpath("requirements-test.txt")

    @property
    def path_requirements_doc(self) -> Path:
        """
        Example: ``${dir_project_root}/requirements-doc.txt``
        """
        return self.dir_project_root.joinpath("requirements-doc.txt")

    @property
    def path_requirements_automation(self) -> Path:
        """
        Example: ``${dir_project_root}/requirements-automation.txt``
        """
        return self.dir_project_root.joinpath("requirements-automation.txt")

    @property
    def path_poetry_lock(self) -> Path:
        """
        Example: ``${dir_project_root}/poetry.lock``
        """
        return self.dir_project_root.joinpath("poetry.lock")

    @property
    def path_poetry_lock_hash_json(self) -> Path:
        """
        Example: ``${dir_project_root}/"poetry-lock-hash.json``
        """
        return self.dir_project_root.joinpath(".poetry-lock-hash.json")

    # ------------------------------------------------------------------------------
    # Build Related
    # ------------------------------------------------------------------------------
    _BUILD_RELATED = None

    @property
    def path_pyproject_toml(self) -> Path:
        """
        Example: ``${dir_project_root}/pyproject.toml``
        """
        return self.dir_project_root.joinpath("pyproject.toml")

    @property
    def dir_build(self) -> Path:
        """
        Example: ``${dir_project_root}/build``
        """
        return self.dir_project_root.joinpath("build")

    @property
    def dir_dist(self) -> Path:
        """
        Example: ``${dir_project_root}/dist``
        """
        return self.dir_project_root.joinpath("dist")
