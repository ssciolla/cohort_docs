# coding=utf-8

from typing import Dict

class Pokémon():

    def __init__(self, poke_dict: Dict):
        self.name = poke_dict['name']
        self.level = poke_dict['level']

    def __str__(self) -> str:
        return self.name
    
    def to_dict(self) -> Dict:
        return self.__dict__
