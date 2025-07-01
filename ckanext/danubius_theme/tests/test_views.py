"""Tests for views.py."""

import pytest


import ckan.plugins.toolkit as tk


@pytest.mark.ckan_config("ckan.plugins", "danubius_theme")
@pytest.mark.usefixtures("with_plugins")
def test_danubius_theme_blueprint(app, reset_db):
    resp = app.get(tk.h.url_for("danubius_theme.page"))
    assert resp.status_code == 200
    assert resp.body == "Hello, danubius_theme!"
