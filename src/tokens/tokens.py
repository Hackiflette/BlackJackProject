import json
import os

import src.common.func_pictures as fct
from src.common.config import ConfigPath


class Tokens:
    data = dict()
    
    @classmethod
    def initialize(cls, file):
        with open(file) as f:
            cls.data = json.load(f)
        
        # Convert key values as integer
        # And load images
        for k in list(cls.data.keys()):
            filename = cls.data.pop(k)
            path = os.path.join(ConfigPath.folder("tokens"), filename)
            cls.data[int(k)] = fct.load_image(path)
    
    @classmethod
    def getImage(cls, value):
        """
        Return the image corresponding to the value
        
        :param value: token value
        :type value: int
        :return: pygame
        :rtype: pygame.Surface
        """

        return cls.data[value]
    
    @classmethod
    def whichTokens(cls, value):
        """
        Return a dictionnary with the token values and their quantity.
        The sum of the tokens being equal to the value.
        
        :param value: researched value
        :type value: int
        :return: dictionnary {value: quantity}
        :rtype: dict
        """

        values = sorted(cls.data.keys(), reverse=True)

        dict_tokens = dict()

        for v in values:
            # If enough
            if value >= v:
                n, value = divmod(value, v)
                dict_tokens[v] = n
        
        return dict_tokens
