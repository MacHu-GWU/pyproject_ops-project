
.. image:: https://readthedocs.org/projects/pyproject_ops/badge/?version=latest
    :target: https://pyproject_ops.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/pyproject_ops-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/pyproject_ops-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/pyproject_ops-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/pyproject_ops-project

.. image:: https://img.shields.io/pypi/v/pyproject_ops.svg
    :target: https://pypi.python.org/pypi/pyproject_ops

.. image:: https://img.shields.io/pypi/l/pyproject_ops.svg
    :target: https://pypi.python.org/pypi/pyproject_ops

.. image:: https://img.shields.io/pypi/pyversions/pyproject_ops.svg
    :target: https://pypi.python.org/pypi/pyproject_ops

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/pyproject_ops-project

------


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://pyproject_ops.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://pyproject_ops.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://pyproject_ops.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/pyproject_ops-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/pyproject_ops-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/pyproject_ops-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/pyproject_ops#files


Welcome to ``pyproject_ops`` Documentation
==============================================================================
This project is my personal folder structure best practice for Python project. It is a replacement of `pygitrepo <https://github.com/MacHu-GWU/pygitrepo-project>`_. The pygitrepo is primarily based on setup.py and requirements.txt file. ``pyproject_ops`` still support the old convention, and also support ``pyproject.toml`` + ``poetry``. It helps you to write less code to do Python development workflow automations. Please check the `pyproject_paths.py <./pyproject_ops/pyproject_paths.py>`_ file to see the folder structure.

This project is hard to test, so I use the vendor pattern (include the source code of this project as it is) in my production project and keep improving it. I will release the stable version to PyPI every three months.


.. _install:

Install
------------------------------------------------------------------------------

``pyproject_ops`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install pyproject_ops

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade pyproject_ops