import certifi
import datetime
import pymongo
from datetime import timezone, datetime
from random import randrange
import os
# db = PetiteUrlDatabase(os.environ['URI'])

class Database:
    def __init__(self):
        """
        Connect Mongodb database and select collection
        :param uri: string with the address and password to connect
        """
        client = pymongo.MongoClient(os.environ['URI'], tlsCAFile=certifi.where())
        my_db = client["sca"]
        self.my_col = my_db["sca_application"]
        # Creates an index just once to make hash_value unique key. If index present, it skips it.
        self.my_col.create_index("application_number", unique=True)

    def insert(self, dict):
        self.my_col.insert_one(dict)

