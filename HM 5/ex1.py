import random

class InvalidParameterError(Exception):
    pass

class InvalidAgeError(InvalidParameterError):
    def __init__(self,age):
        super().__init__(self.age)

class InvalidSoundError(InvalidParameterError):
    def __init__(self,sound):
        super().__init__(self.sound)

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} makes {self.sound}")

    def print(self):
        pass
    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self):
        super.__init__()
        if self.age >15:
            raise InvalidAgeError
        if self.sound.count("r") < 2:
            raise InvalidSoundError
    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i])}")

class Lemur(JungleAnimal):
    def __init__(self):
        super.__init__()
        if self.age >10:
            raise InvalidAgeError
        if self.sound.count("e") < 1:
            raise InvalidSoundError

    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")
    def daily_task(self, fruits):
        if fruits > 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            return fruits-10
        else:
            print(f"{self.name} the Lemur could only find {fruits} fruits")
            return 0

class Human(JungleAnimal):
    def __init__(self):
        super.__init__()
        if self.age >10:
            raise InvalidAgeError
        if self.sound.count("e") < 1:
            raise InvalidSoundError
    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")
    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if animals[i] == self:
                if i != 0 and i != len(animals) - 1:
                    if type(animals[i + 1]) == Human or type(animals[i - 1]) == Human:
                        type = input(f"Enter type: ")
                        buildings.append(Building(type))


class Building():
    def __init__(self, type):
        self.type = type

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]


for i in range(102):
    p = random.randint(0, 9)
    if 0 <= p <= 3:
        animals.append(Lemur(names[random.randint(0, len(names))]), random.randint(0, 20), sounds[random.randint(0, len(sounds))])
    elif 3 <= p <= 7:
        animals.append(Jaguar(names[random.randint(0, len(names))]), random.randint(0, 20), sounds[random.randint(0, len(sounds))])
    elif 8 <= p <= 9:
        animals.append(Human(names[random.randint(0, len(names))]), random.randint(0, 20), sounds[random.randint(0, len(sounds))])
print(f"The jungle now has {len(animals)} animals")


for anim in animals:
	anim.daily_task()


print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)