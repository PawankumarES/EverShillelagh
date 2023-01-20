# Taken from: https://github.com/apache/superset/blob/master/superset/db_engine_specs/gsheets.py
from superset.db_engine_specs.sqlite import SqliteEngineSpec


class EverstageEngineSpec(SqliteEngineSpec):
    """Engine for Everstage API tables"""

    engine = "everstage"
    engine_name = "Everstage"
    allows_joins = True
    allows_subqueries = True

    default_driver = "apsw"
    sqlalchemy_uri_placeholder = "everstage://"
