class Settings:
    BFX_KEY = data['BFX_KEY']
    BFX_SECRET = data['BFX_SECRET']
    MONGO_CLIENT = os.environ['MONGODB_CLIENT']
    MONGO_DB = os.environ['BFX_FEE_DB']
    PRIORITY_ORDERS = orders['data']
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
