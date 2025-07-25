import yaml
import os

def load_config(config_file: str = "config/config.yaml"):
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
    return config