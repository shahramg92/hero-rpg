
from characters.base import CharacterBase

class WereWolf (CharacterBase):
    def __init__ (self, name):
        super().__init__(name)
        self.health = 10

    def greet (self):
        super().greet()
        print('AAHHHHH')
