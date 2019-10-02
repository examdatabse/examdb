import lfu

MAX_CAPACITY = 10000


class Cache:
    _cache = lfu.LFUCache(MAX_CAPACITY)

    def __init__(self):
        pass

    def put(self, key, value):
        self._cache.set(key, value)

    def get(self, key):
        return self._cache.get(key)

    def contain(self, key):
        return self._cache.is_in_cache(key)
