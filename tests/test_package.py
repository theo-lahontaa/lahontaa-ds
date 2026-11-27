"""Smoke tests: the package is installed and importable."""

from importlib.metadata import version

import lahontaa_ds


def test_package_has_docstring():
    assert lahontaa_ds.__doc__ == "Personal Python toolkit for data science."


def test_package_metadata_is_installed():
    assert version("lahontaa-ds")