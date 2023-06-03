
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
There are many different folder structures for Python project. I have my personal best practice based on Python career experience. This project is an automation tools that can do a lot of common tasks for Python project development life cycle, such as: "create virtualenv", "install dependencies", "run test", "build documentation site", etc ...

A little history about this project:

    I had an automation tool `pygitrepo <https://github.com/MacHu-GWU/pygitrepo-project>`_ for my old development workflow. The pygitrepo is primarily based on setup.py and requirements.txt file. ``pyproject_ops`` still support the old convention, and also support ``pyproject.toml`` + ``poetry``. It helps me to write less code to do Python development workflow automations. Please check the `pyproject_paths.py <./pyproject_ops/pyproject_paths.py>`_ file to see the folder structure.

This project is hard to test, so I use the vendor pattern (include the source code of this project as it is) in my production project and keep improving it. I will release the stable version to PyPI every three months.

- `pyproject_ops.py <./pyproject_ops/pyproject_ops.py>`_:
- `pyproject_build.py <./pyproject_ops/pyproject_build.py>`_:
- `pyproject_deps.py <./pyproject_ops/pyproject_deps.py>`_:
- `pyproject_docs.py <./pyproject_ops/pyproject_docs.py>`_:
- `pyproject_ops.py <./pyproject_ops/pyproject_ops.py>`_:
- `pyproject_paths.py <./pyproject_ops/pyproject_paths.py>`_:
- `pyproject_tests.py <./pyproject_ops/pyproject_tests.py>`_:
- `pyproject_venv.py <./pyproject_ops/pyproject_venv.py>`_:

.. _install:

Install
------------------------------------------------------------------------------

``pyproject_ops`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install pyproject_ops

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade pyproject_ops