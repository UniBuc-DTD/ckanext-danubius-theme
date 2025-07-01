from flask import Blueprint


danubius_theme = Blueprint(
    "danubius_theme", __name__)


def page():
    return "Hello, danubius_theme!"


danubius_theme.add_url_rule(
    "/danubius_theme/page", view_func=page)


def get_blueprints():
    return [danubius_theme]
