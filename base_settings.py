import os

import sys

class BaseSettings:
    MONGO_CLIENT = os.environ.get('MONGODB_CLIENT')
    MONGO_DB = os.environ.get('BFX_FEE_DB')

    if len(sys.argv) > 1 and sys.argv[1] == 'localhost':
        REDIS_HOST = 'localhost'
    REDIS_HOST = 'redis-cluster-ip-service'

    REDIS_PORT = 6379
