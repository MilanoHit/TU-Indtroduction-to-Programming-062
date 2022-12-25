from .Item import item
class weapon(item):

    def __init__(self, attack, name):
        super().__init__(self, name)
        self.attack = attack
