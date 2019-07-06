import json
import os


class ConfigPath:
    path = dict()

    @classmethod
    def initialize(cls, path):
        with open(path, encoding="utf-8") as f:
            cls.path = json.load(f)
    
    @classmethod
    def get(cls, *keys):
        """
        Return the value after each key.

        ..Example:
            ConfigPath.get("folder", "data")
        
        :return: value in the path config file
        :rtype: any json storage type
        """

        config = cls.path
        for key in keys:
            config = config[key]
        return os.path.join(*config)
    
    @classmethod
    def folder(cls, key):
        """
        Return the path to the folder given by its name
        
        :param str key: folder name
        :return: folder path
        :rtype: str
        """
        return cls.get("folders", key)
