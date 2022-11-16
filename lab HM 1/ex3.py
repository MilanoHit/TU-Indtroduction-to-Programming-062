n = input()

dict = {}

for character in n:
    if character not in dict.keys():
        dict.update({character : n.count(character)})

print(dict)