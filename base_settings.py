import os


class BaseSettings:
    MONGO_CLIENT = os.environ['MONGODB_CLIENT']
    MONGO_DB = os.environ['BFX_FEE_DB']
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
