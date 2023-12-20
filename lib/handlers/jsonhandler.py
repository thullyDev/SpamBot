import json
import os

class JsonHandler:
    def load_json(self, filename):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\lib", "")
        filepath = os.path.join(base_dir, 'jsons', f"{filename}.json")

        with open(filepath, 'r') as file:
            data = json.load(file)

        return data

    def write_json(self, data, filename):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace("\\lib", "")
        filepath = os.path.join(base_dir, 'jsons', f"{filename}.json")

        with open(filepath, 'w') as file:
            json.dump(data, file, indent=2)
