# rotes/__init__.py.
# flake8: noqa

from .home import home_blueprints
from .directories import directories_blueprints
from .table_routes import table_blueprints

blueprints = home_blueprints | directories_blueprints | table_blueprints
