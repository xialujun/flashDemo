import sys

from .config import config

from . import (
    db_is_ready,
    create_user,
    create_db
)

if len(sys.argv) == 2 and sys.argv[1] == "print":
    config.print()
    sys.exit(0)

if db_is_ready():
    create_user()
    create_db()
