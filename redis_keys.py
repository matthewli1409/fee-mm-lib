from enum import Enum


class RedisKey(Enum):
    """Redis keys"""
    SYMBOLS_SUBBED = 'symbols-subbed'
    SYMBOLS_WALLET = 'symbols-wallet'
