from Errors import InvalidCharacterClass, InvalidDataFormat
from .Weapon import weapon
from .Item import item


class hero():
    roles = "Warrior", "Priest", "Rogue", "Mage"
    
    def __init__(self, name, gender, role):
        self.name = name
        self.gender = gender
        if gender != "male" and gender != "female":
            raise InvalidDataFormat()
        if role not in self.roles:
            raise InvalidCharacterClass()
        self.role = role

    def add_weapon(self, name, attack):
        if attack < 0:
            raise InvalidDataFormat()
        self.weapon = weapon(name, attack)

    def add_item(self, name):
        self.name = item(name)