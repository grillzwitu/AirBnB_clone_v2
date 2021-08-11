#!/usr/bin/python3
"""This module creates a unique storage class"""

from os import getenv

storage_t = getenv("HBNB_TYPE_STORAGE")

# check envirn var to determine storage method
if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:  # file storage selected
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
