"""
Plugin tests.
"""

import pytest

import ckan.plugins as p
from ckan.lib.helpers import url_for
import ckan.tests.helpers as helpers

@pytest.mark.usefixtures("with_plugins")
class TestPlugin:
    def test_sanity_check(self):
        assert True

    def test_plugin_loads(self):
        plugin = p.get_plugin("danubius_theme")
        assert plugin

    @pytest.mark.ckan_config("ckan.plugins", "spatial_metadata spatial_query danubius_theme")
    @pytest.mark.usefixtures("clean_db", "clean_index")
    def test_search_page_renders(self, app):
        response = app.get(url_for("dataset.search"))
        assert helpers.body_contains(response, "Filter by location")
