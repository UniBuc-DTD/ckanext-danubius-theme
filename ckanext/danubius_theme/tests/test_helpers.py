"""Tests for helpers.py."""

import ckanext.danubius_theme.helpers as helpers


def test_danubius_theme_hello():
    assert helpers.danubius_theme_hello() == "Hello, danubius_theme!"
