def input_nums(n):
    if type(n) == int or (type(n) == str and n.isnumeric()):
        n = int(n)
        arr = []
        for i in range(n):
            el = input()
            if el.isnumeric():
                arr.append(int(el))
        return arr

    arr = []
    return arr


def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
        el_is_float = True
        if type(lst[i]) == str:
            for character in lst[i]:
                if (character < "0" or character) > "9" and character != ".":
                    el_is_float = False
                    break
        if type(lst[i]) == int or el_is_float or type(lst[i]) == float:
            sum += float(lst[i])
    return sum

def max_of_two(a, b):
    a_is_float = True
    b_is_float = True
    if type(a) == str:
        for character in a:
            if (character < "0" or character) > "9" and character != ".":
                a_is_float = False
                break
    if type(b) == str:
        for character in b:
            if (character < "0" or character > "9") and character != ".":
                b_is_float = False
                break
    if (type(a) == int or a_is_float or type(a) == float) and (type(b) == int or b_is_float or type(b) == float):
        if float(a) >= float(b):
            print(float(a), float(b))
            return a
        else:
            return b
    elif type(a) == int or (type(a) == str and a.isdigit()) or type(a) == float:
        return a
    elif type(b) == int or (type(b) == str and b.isdigit()) or type(b) == float:
        return b
    return


print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))