from Entitiess.Hero import hero
from Entitiess.Item import item
from Entitiess.Weapon import weapon

class Menu:

    def print_menu(self):
        print(" 1. Create a new character")
        print(" 2. Add a weapon to a character")
        print(" 3. Add an item to a character")
        print(" 4. List all characters")
        print(" 5. Delete a character")
        print(" Exit")

    def run(self):
        heroes = []


        while True:
            self.print_menu()
            command = input()
            try:
                if command == "1":
                    self.add_Hero(heroes)
                elif command == "2":
                    self.add_weapon(heroes)
                elif command == "3":
                    self.add_Item(heroes)
                elif command == "4":
                    self.print_all(heroes)
                elif command == "5":
                    self.delete_character(heroes)
                elif command == "Exit":
                    break
                else:
                    raise InvalidCommand()
            except Exception as e:
                print(f"Error: {str(e)}")

    def add_Hero(self, heroes):
        name = input("Enter name: ")
        gender = input("Enter gender: ")
        role = input("Enter class: ")
        heroes.append(hero(name, gender, role))

    def add_weapon(self, heroes):
        name = input("Enter name of character: ")
        character = self.find_character(heroes, name)
        name_weapon = input("Enter name of weapon: ")
        attack = input("Enter attack of weapon: ")
        character.add_weapon(attack, name_weapon)
    
    def add_Item(self, heroes):
        name = input("Enter name of character: ")
        character = self.find_character(heroes, name)
        Item_name = input("Enter name of item: ")
        character.add_item(Item_name)

    def find_character(self, heroes, name) -> hero:
        for i in range(len(heroes)):
            if name == heroes[i].name:
                return heroes[i]
        else:
            raise CharacterNotFound()

    def delete_character(self, heroes):
        name = input("Enter name of character: ")
        for i in range(len(heroes)):
            if heroes[i].name == name:
                heroes.pop(i)
        else:
            raise CharacterNotFound()
        
    def print_all(self, heroes):
        for i in range(len(heroes)):
            print(f"{heroes[i].name} {heroes[i].gender} {heroes[i].weapon.name} {heroes[i].item.name}")

if __name__ == '__main__':
    menu = Menu()
    menu.run()