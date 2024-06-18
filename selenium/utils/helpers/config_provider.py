import os
from configparser import ConfigParser

from project_constants import project_path


def __config_provider_builder(config_name):
    """
    Read all section and values from ini files
    """
    config = ConfigParser()
    config_path = os.path.join(project_path, config_name)
    config.read(config_path)
    dictionary = {}
    for section in config:
        all_items = dict(config.items(section))
        for key, value in all_items.items():
            dictionary[key] = value
    return dictionary


settings_config = __config_provider_builder("config.ini")
