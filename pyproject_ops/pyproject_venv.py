# -*- coding: utf-8 -*-

import typing as T
import shutil
import subprocess
import dataclasses


if T.TYPE_CHECKING:
    from .pyproject_ops import PyProjectOps


@dataclasses.dataclass
class PyProjectVenv:
    """
    :param python_version: example "3.7", "3.8", ...
    """

    python_version: str = dataclasses.field()

    def create_virtualenv(self: "PyProjectOps") -> bool:
        """
        .. code-block:: bash

            $ virtualenv -p python${X}.${Y} ./.venv

        :return: a boolean flat to indicate whether a creation is performed.
        """
        if self.dir_venv.exists():
            return False
        else:
            subprocess.run(
                [
                    f"{self.path_bin_virtualenv}",
                    "-p",
                    f"python{self.python_version}",
                    f"{self.dir_venv}",
                ],
                check=True,
            )
            return True

    def remove_virtualenv(self: "PyProjectOps") -> bool:
        """
        .. code-block:: bash

            $ rm -r ./.venv

        :return: a boolean flat to indicate whether a deletion is performed.
        """
        if self.dir_venv.exists():
            shutil.rmtree(f"{self.dir_venv}", ignore_errors=True)
            return True
        else:
            return False
