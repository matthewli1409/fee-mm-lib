import os
import sys

BFX_API_KEY = os.environ['BFX_MM_FEE_KEY_1']
BFX_API_SECRET = os.environ['BFX_MM_FEE_SECRET_1']

MONGO_CLIENT = os.environ['MONGODB_CLIENT']
MONGO_DB = os.environ['BFX_FEE_DB']

if len(sys.argv) > 1 and sys.argv[1] == 'localhost':
    REDIS_HOST = 'localhost'
else:
    REDIS_HOST = 'redis-cluster-ip-service'

REDIS_PORT = 6379
