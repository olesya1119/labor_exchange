# rotes/__init__.py.
# flake8: noqa

from .home import home_blueprints
from .directories import directories_blueprints
from .table_routes import table_blueprints
from .intermediate_tables import intermediate_tables_blueprints
from .help import help_blueprints
from .various import various_blueprints
from .documents import documents_blueprints

blueprints = home_blueprints | directories_blueprints | table_blueprints | intermediate_tables_blueprints | help_blueprints | various_blueprints | documents_blueprints
