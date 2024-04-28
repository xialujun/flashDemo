import logging

from psycopg2 import sql
from psycopg2.errors import (
    DuplicateObject,
    DuplicateDatabase
)


logger = logging.getLogger(__name__)


class SqlQuery:
    def __init__(self, connection, config):
        self.connection = connection
        self.config = config

    def create_user(self):
        query = sql.SQL(
            "CREATE USER {user} WITH ENCRYPTED PASSWORD '{password}';"
        ).format(
            user=sql.Identifier(self.config.user),
            password=sql.Identifier(self.config.password)
        )
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query)
                print("created")
                self.connection.commit()
            except DuplicateObject:
                logger.error(f"User {self.config.user} already exists")

    def create_db(self):
        query = sql.SQL(
            "CREATE DATABASE {database} WITH OWNER {user}"
        ).format(
            user=sql.Identifier(self.config.user),
            database=sql.Identifier(self.config.database)
        )

        self.connection.autocommit = True  # required by CREATE DATABASE
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query)
                self._grant_all_priv()
                self.connection.commit()
            except DuplicateDatabase:
                logger.error(f"Database {self.config.database} already exists")

    def _grant_all_priv(self):
        query = sql.SQL(
            "GRANT ALL PRIVILEGES ON DATABASE {database} TO {user};"
        ).format(
            database=sql.Identifier(self.config.database),
            user=sql.Identifier(self.config.user)
        )

        with self.connection.cursor() as cursor:
            cursor.execute(query)
