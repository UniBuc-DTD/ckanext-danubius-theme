[![CI](https://github.com/UniBuc-DTD/ckanext-danubius-theme/workflows/Continuous%20Integration/badge.svg?branch=main)](https://github.com/UniBuc-DTD/ckanext-danubius-theme/actions)

# DANUBIUS CKAN Theme

This repository contains a custom [CKAN](https://ckan.org/) theme with the branding of the [DANUBIUS](https://danubius-ri.eu) consortium. It is meant to be used on the [DANUBIUS Data Portal](https://data.danubius-ri.eu).

## Requirements

Requires the latest (stable) version of CKAN, which at the time of writing is CKAN 2.11. We only use the latest version in production and do not test this theme with older versions.

## Installation

Note that some of the components of this theme (e.g. the search page) rely on having the [`ckanext-spatial`](https://docs.ckan.org/projects/ckanext-spatial/en/latest/) plugin active.
Please see [the `ckanext-spatial` installation instructions](https://docs.ckan.org/projects/a-spatial/en/latest/install/) for guidance.

To install `ckanext-danubius-theme`:

1. Activate your CKAN virtual environment, for example:

     source /usr/lib/ckan/default/bin/activate

2. Clone the source and install it on the virtualenv

    git clone https://github.com/UniBuc-DTD/ckanext-danubius-theme.git
    cd ckanext-danubius-theme
    pip install -e .
	pip install -r requirements.txt

3. Add `danubius_theme` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with NGINX on Ubuntu:

     sudo systemctl reload nginx


## Config settings

None at the moment.

## Developer installation

To install `ckanext-danubius-theme` for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/UniBuc-DTD/ckanext-danubius-theme.git
    cd ckanext-danubius-theme
    pip install -e .
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini

## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
