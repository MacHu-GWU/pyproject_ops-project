# -*- coding: utf-8 -*-

"""
This module automates dependencies management.

We use `Python poetry <https://python-poetry.org/>`_ to ensure determinative dependencies.
"""

import typing as T
import json
import subprocess
import dataclasses
from pathlib import Path

from .helpers import sha256_of_bytes


if T.TYPE_CHECKING:
    from .pyproject_ops import PyProjectOps


def _quite_pip_install_in_ci(args: T.List[str]):
    """
    Add a cli argument to disable output for ``pip install`` command.

    We only need to disable ``pip install`` output in CI, because we don't
    want to see long list of installation messages in CI.
    """
    args.append("--disable-pip-version-check")
    args.append("--quiet")


@dataclasses.dataclass
class PyProjectDeps:
    def poetry_lock(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            poetry lock

        This command will resolve the dependencies defined in the ``pyproject.toml``
        file, and write the resolved versions to the ``poetry.lock`` file.
        You have to run this everytime you changed the ``pyproject.toml`` file.
        And you should commit the latest ``poetry.lock`` file to git.

        Ref:

        - poetry lock: https://python-poetry.org/docs/cli/#lock
        """
        with self.dir_project_root.temp_cwd():
            subprocess.run([f"{self.path_bin_poetry}", "lock"])

    def poetry_install(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            poetry install

        Ref:

        - poetry install: https://python-poetry.org/docs/cli/#install
        """
        subprocess.run([f"{self.path_bin_poetry}", "install"], check=True)

    def poetry_install_dev(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            poetry install --with dev

        Ref:

        - poetry install: https://python-poetry.org/docs/cli/#install
        """
        subprocess.run(
            [f"{self.path_bin_poetry}", "install", "--with", "dev"], check=True
        )

    def poetry_install_test(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            poetry install --with test

        Ref:

        - poetry install: https://python-poetry.org/docs/cli/#install
        """
        subprocess.run(
            [f"{self.path_bin_poetry}", "install", "--with", "test"], check=True
        )

    def poetry_install_doc(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            poetry install --with doc

        Ref:

        - poetry install: https://python-poetry.org/docs/cli/#install
        """
        subprocess.run(
            [f"{self.path_bin_poetry}", "install", "--with", "doc"], check=True
        )

    def poetry_install_all(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-automation.txt
            poetry install
            poetry install --with dev,test,doc

        Ref:

        - poetry install: https://python-poetry.org/docs/cli/#install
        """
        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_automation}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)
        subprocess.run([f"{self.path_bin_poetry}", "install"], check=True)
        subprocess.run(
            [f"{self.path_bin_poetry}", "install", "--with", "dev,test,doc"], check=True
        )

    def _do_we_need_poetry_export(
        self: "PyProjectOps", current_poetry_lock_hash: str
    ) -> bool:
        """
        ``poetry export`` is an expensive command. We would like to use cache
        mechanism to avoid unnecessary export.

        Everytime we run :func:`_poetry_export`, at the end, it will write the
        sha256 hash of the ``poetry.lock`` to the ``.poetry-lock-hash.json`` cache file.
        It locates at the repo root directory. This function will compare the
        sha256 hash of the current ``poetry.lock`` to the value stored in the cache file.
        If they don't match, it means that the ``poetry.lock`` has been changed,
        so we should run :func:`_poetry_export` again.

        The content of ``.poetry-lock-hash.json`` looks like::

            {
                "hash": "sha256-hash-of-the-poetry.lock-file",
                "description": "DON'T edit this file manually!"
            }

        Ref:

        - poetry export: https://python-poetry.org/docs/cli/#export

        :param current_poetry_lock_hash: the sha256 hash of the current ``poetry.lock`` file
        """
        if self.path_poetry_lock_hash_json.exists():
            # read the previous poetry lock hash from cache file
            cached_poetry_lock_hash = json.loads(
                self.path_poetry_lock_hash_json.read_text()
            )["hash"]
            return current_poetry_lock_hash != cached_poetry_lock_hash
        else:
            # do poetry export if the cache file not found
            return True

    def _poetry_export_group(self: "PyProjectOps", group: str, path: Path):
        """
        Export dependency group to given file.

        :param group: dependency group name, for example dev dependencies are defined
            in the ``[tool.poetry.group.dev]`` and ``[tool.poetry.group.dev.dependencies]``
            sections of he ``pyproject.toml`` file.
        :param path: the path to the exported ``requirements.txt`` file.
        """
        subprocess.run(
            [
                f"{self.path_bin_poetry}",
                "export",
                "--format",
                "requirements.txt",
                "--output",
                f"{path}",
                "--only",
                group,
            ],
            check=True,
        )

    def _poetry_export(self: "PyProjectOps", current_poetry_lock_hash: str):
        """
        Run ``poetry export --format requirements.txt ...`` command and write
        the sha256 hash of the current ``poetry.lock`` file to the cache file.

        :param current_poetry_lock_hash: the sha256 hash of the current ``poetry.lock`` file
        """
        # export the main dependencies
        self.path_requirements_main.remove_if_exists()
        subprocess.run(
            [
                f"{self.path_bin_poetry}",
                "export",
                "--format",
                "requirements.txt",
                "--output",
                f"{self.path_requirements_main}",
            ],
            check=True,
        )

        # export dev, test, doc dependencies
        for group, path in [
            ("dev", self.path_requirements_dev),
            ("test", self.path_requirements_test),
            ("doc", self.path_requirements_doc),
        ]:
            path.remove_if_exists()
            self._poetry_export_group(group, path)

        # write the ``poetry.lock`` hash to the cache file
        self.path_poetry_lock_hash_json.write_text(
            json.dumps(
                {
                    "hash": current_poetry_lock_hash,
                    "description": "DON'T edit this file manually!",
                },
                indent=4,
            )
        )

    def poetry_export(self: "PyProjectOps") -> bool:
        """
        :return: ``True`` if ``poetry export`` is executed, ``False`` if not.
        """
        poetry_lock_hash = sha256_of_bytes(self.path_poetry_lock.read_bytes())
        if self._do_we_need_poetry_export(poetry_lock_hash):
            self._poetry_export(poetry_lock_hash)
            return True
        else:
            return False

    def _try_poetry_export(self: "PyProjectOps"):
        """
        This is a silent version of :func:`poetry_export`. It is called before
        running ``pip install -r requirements-***.txt`` command. It ensures that
        those exported ``requirements-***.txt`` file exists.
        """
        if self.path_poetry_lock.exists() is False:
            return

        poetry_lock_hash = sha256_of_bytes(self.path_poetry_lock.read_bytes())
        if self._do_we_need_poetry_export(poetry_lock_hash):
            self._poetry_export(poetry_lock_hash)

    def pip_install(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -e . --no-deps

        Ref:

        - pip install: https://pip.pypa.io/en/stable/cli/pip_install/#options
        """
        self._try_poetry_export()

        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-e",
            f"{self.dir_project_root}",
            "--no-deps",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_main}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

    def pip_install_dev(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-dev.txt
        """
        self._try_poetry_export()

        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_dev}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

    def pip_install_test(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-test.txt
        """
        self._try_poetry_export()

        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_test}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

    def pip_install_doc(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-doc.txt
        """
        self._try_poetry_export()

        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_doc}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

    def pip_install_automation(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-automation.txt
        """
        args = [
            f"{self.path_venv_bin_pip}",
            "install",
            "-r",
            f"{self.path_requirements_automation}",
        ]
        _quite_pip_install_in_ci(args)
        subprocess.run(args, check=True)

    def pip_install_all(self: "PyProjectOps"):
        """
        Run:

        .. code-block:: bash

            pip install -r requirements-main.txt
            pip install -r requirements-dev.txt
            pip install -r requirements-test.txt
            pip install -r requirements-doc.txt
            pip install -r requirements-automation.txt
        """
        self._try_poetry_export()

        subprocess.run(
            [
                f"{self.path_venv_bin_pip}",
                "install",
                "-e",
                f"{self.dir_project_root}",
                "--no-deps",
            ],
            check=True,
        )

        for path in [
            self.path_requirements_main,
            self.path_requirements_dev,
            self.path_requirements_test,
            self.path_requirements_doc,
            self.path_requirements_automation,
        ]:
            args = [f"{self.path_venv_bin_pip}", "install", "-r", f"{path}"]
            _quite_pip_install_in_ci(args)
            subprocess.run(args, check=True)
