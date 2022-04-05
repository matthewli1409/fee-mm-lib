import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--LOCALHOST', type=str, required=False)
args = parser.parse_args()

MONGO_CLIENT = os.environ.get('MONGODB_CLIENT')
MONGO_DB = os.environ.get('BFX_FEE_DB')

REDIS_PORT = 6379

if args.LOCALHOST:
    REDIS_HOST = 'localhost'
else:
    REDIS_HOST = 'redis-svc'
