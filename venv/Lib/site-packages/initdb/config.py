import logging
import os

__all__ = [
    'config', 'Config'
]

logger = logging.getLogger(__name__)


class Config:
    """
    Contains all parameters required by the application
    """

    def __init__(self):
        self.host = os.environ.get(
            "PAPERMERGE_DATABASE_HOST",
            "postgres"
        )
        # initial_user and initial_password are used to
        # check if database is up and running
        self.initial_user = os.environ.get(
            "INITIAL_DATABASE_USER",
            "postgres"
        )
        self.initial_password = os.environ.get(
            "INITIAL_DATABASE_PASSWORD",
            None
        )
        self.user = os.environ.get(
            "PAPERMERGE_DATABASE_USER",
            None
        )
        self.database = os.environ.get(
            "PAPERMERGE_DATABASE_NAME",
            None
        )
        self.password = os.environ.get(
            "PAPERMERGE_DATABASE_PASSWORD",
            None
        )
        self.port = os.environ.get(
            "PAPERMERGE_DATABASE_PORT",
            5432
        )

    def print(self):
        logger.info(f"host={self.host}")
        logger.info(f"port={self.port}")
        logger.info(f"initial_user={self.initial_user}")
        logger.info(f"initial_pass={self.initial_password}")
        logger.info(f"user={self.user}")
        logger.info(f"database={self.database}")
        logger.info(f"pass={self.password}")

    def __str__(self):
        return f"Config(host={self.host}, port={self.port})"


config = Config()
