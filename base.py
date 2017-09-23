class CharacterBase:
    def __init__ (self, name):
        self.name = name

    def greet (self):
        print('Hello there', self.name)
