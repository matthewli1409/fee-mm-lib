import os
import sys

MONGO_CLIENT = os.environ['MONGODB_CLIENT']
MONGO_DB = os.environ['BFX_FEE_DB']

# STATIC - DON'T CHANGE UNLESS YOU KNOW WHAT YOU ARE DOING
if len(sys.argv) > 1 and sys.argv[1] == 'localhost':
    REDIS_HOST = 'localhost'
else:
    REDIS_HOST = 'redis-cluster-ip-service'

REDIS_PORT = 6379
