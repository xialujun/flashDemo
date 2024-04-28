from .config import config
from .utils import db_is_ready as _db_is_ready
from .utils import create_user as _create_user
from .utils import create_db as _create_db

__all__ = [
    'db_is_ready',
    'create_db',
    'create_user'
]


def db_is_ready():
    return _db_is_ready(config)


def create_user():
    return _create_user(config)


def create_db():
    return _create_db(config)
