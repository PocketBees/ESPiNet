import json

def load_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

def save_config(filename, config):
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)

# Example usage for updating and saving configuration
config['servos']['pan']['safe_range']['min'] = 2.0
save_config('config.json', config)

# Usage
config = load_config('config.json')
print(config['servos']['pan']['safe_range']['min'])  # Example of accessing the pan servo's min safe range