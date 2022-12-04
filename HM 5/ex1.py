import random


class InvalidParameterError(Exception):
    pass


class InvalidAgeError(InvalidParameterError):
    def __init__(self, age):
        super().__init__(age)


class InvalidSoundError(InvalidParameterError):
    def __init__(self, sound):
        super().__init__(sound)


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
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 15:
            raise InvalidAgeError(age)
        if self.sound.count("r") < 2:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals):
        for i in range(len(animals)):
            if type(animals[i]) == Lemur or type(animals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {animals[i].name} the {type(animals[i]).__name__}")
                animals.pop(i)
                break


class Lemur(JungleAnimal):

    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >10:
            raise InvalidAgeError(age)
        if self.sound.count("e") < 1:
            raise InvalidSoundError(sound)

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
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age >10:
            raise InvalidAgeError(age)
        if self.sound.count("e") < 1:
            raise InvalidSoundError(sound)

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, animals, buildings):
        for i in range(len(animals)):
            if animals[i] == self:
                if i != 0 and i != len(animals) - 1:
                    if type(animals[i + 1]) == Human or type(animals[i - 1]) == Human:
                        type1 = input(f"Enter type: ")
                        buildings.append(Building(type1))


class Building():
    def __init__(self, type1):
        self.type1 = type1
    def print(self):
        print(self.type1)

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
    try:
        if 0 <= p <= 3:
            k = random.randint(0, 20)
            name = random.randint(0, len(names) - 1)
            sound = random.randint(0, len(sounds) - 1)
            animals.append(Lemur(names[name], k, sounds[sound]))
        elif 3 <= p <= 7:
            k = random.randint(0, 20)
            name = random.randint(0, len(names) - 1)
            sound = random.randint(0, len(sounds) - 1)
            animals.append(Jaguar(names[name], k, sounds[sound]))
        elif 8 <= p <= 9:
            k = random.randint(0, 20)
            name = random.randint(0, len(names) - 1)
            sound = random.randint(0, len(sounds) - 1)
            animals.append(Human(names[name], k, sounds[sound]))
    except InvalidSoundError:
        print("Invalid Sound")
    except InvalidAgeError:
        print("Invalid Age")
print(f"The jungle now has {len(animals)} animals")


for anim in animals:
    if type(anim) == Lemur:
        fruits = random.randint(1, 20)
        anim.daily_task(fruits)
    elif type(anim) == Jaguar:
        anim.daily_task(animals)
    elif type(anim) == Human:
        anim.daily_task(animals, buildings)

print(f"The jungle now has {len(animals)} animals")

for i in range(len(animals)):
    animals[i].print()

for i in range(len(buildings)):
    buildings[i].print()