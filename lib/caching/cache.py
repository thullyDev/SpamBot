from ..handlers.jsonhandler import JsonHandler

class Cache(JsonHandler):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Cache, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.cachemap = self.load_json(filename="cache")

    def set(self, key, data):
        self.cachemap[key] = data
        self.save()

    def get(self, key, default=None):
        return self.cachemap.get(key, default)

    def update(self, key, data):
        old_data = self.get(key, {})
        for ky, val in data.items():
            old_data[ky] = val
        self.set(key, old_data)

    def delete(self, key):
        del self.cachemap[key]
        self.save()

    def save(self):
        self.write_json(filename="cache", data=self.cachemap)
