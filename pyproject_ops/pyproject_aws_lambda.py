# -*- coding: utf-8 -*-

import typing as T
import dataclasses
from pathlib_mate import Path


if T.TYPE_CHECKING:
    from .ops import PyProjectOps


@dataclasses.dataclass
class PyProjectAWSLambda:
    @property
    def dir_build_lambda(self: "PyProjectOps") -> Path:
        """
        Example: ``${dir_project_root}/build/lambda``
        """
        return self.dir_build.joinpath("lambda")

    @property
    def dir_build_lambda_python(self) -> Path:
        """
        Example: ``${dir_project_root}/build/lambda/python``
        """
        return self.dir_build_lambda.joinpath("python")

    @property
    def path_build_lambda_bin_aws(self) -> Path:
        """
        Example: ``${dir_project_root}/build/lambda/python/aws``
        """
        return self.dir_build_lambda_python.joinpath("aws")

    @property
    def path_build_lambda_source_zip(self) -> Path:
        """
        Example: ``${dir_project_root}/build/lambda/source.zip``
        """
        return self.dir_build_lambda.joinpath("source.zip")

    @property
    def path_build_lambda_layer_zip(self) -> Path:
        """
        Example: ``${dir_project_root}/build/lambda/layer.zip``
        """
        return self.dir_build_lambda.joinpath("layer.zip")

    @property
    def dir_lambda_app(self: "PyProjectOps") -> Path:
        """
        Example: ``${dir_project_root}/lambda_app``
        """
        return self.dir_project_root.joinpath("lambda_app")

    @property
    def path_chalice_config(self) -> Path:
        """
        Example: ``${dir_project_root}/lambda_app/.chalice/config.json``
        """
        return self.dir_lambda_app.joinpath(".chalice", "config.json")

    @property
    def dir_lambda_app_vendor(self) -> Path:
        """
        Example: ``${dir_project_root}/lambda_app/vendor``
        """
        return self.dir_lambda_app.joinpath("vendor")

    @property
    def dir_lambda_app_deployed(self) -> Path:
        """
        Example: ``${dir_project_root}/lambda_app/.chalice/deployed``
        """
        return self.dir_lambda_app.joinpath(".chalice", "deployed")

    @property
    def path_lambda_update_chalice_config_script(self) -> Path:
        """
        Example: ``${dir_project_root}/lambda_app/update_chalice_config.py``
        """
        return self.dir_lambda_app.joinpath("update_chalice_config.py")

    @property
    def path_lambda_app_py(self) -> Path:
        """
        Example: ``${dir_project_root}/lambda_app/app.py``
        """
        return self.dir_lambda_app.joinpath("app.py")
