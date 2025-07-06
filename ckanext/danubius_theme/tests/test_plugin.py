"""
Tests for plugin.py.
"""

import pytest


@pytest.mark.ckan_config("ckan.plugins", "danubius_theme")
@pytest.mark.usefixtures("with_plugins")
def test_sanity_check():
    assert True
