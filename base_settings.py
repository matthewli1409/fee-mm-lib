import os

import sys

class BaseSettings:
    MONGO_CLIENT = os.environ.get('MONGODB_CLIENT')
    MONGO_DB = os.environ.get('BFX_FEE_DB')
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
