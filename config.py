# config.py
import json

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.settings = self.load_config()

    def load_config(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def get_setting(self, key_path):
        """Retrieve a setting value by specifying a path of keys."""
        setting = self.settings
        for key in key_path:
            setting = setting.get(key, None)
            if setting is None:
                break
        return setting

# Usage
from config import Config

config = Config('config.json')
pan_min = config.get_setting(['servos', 'pan', 'safe_range', 'min'])