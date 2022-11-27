def  list_avg(lst, mlt = 1):
    for i in range(len(lst)):
        lst[i] *= mlt
    avg = 0
    count = 0
    for i in range(len(lst)):
        if type(lst[i]) == int:
            avg += lst[i]
            count += 1

    avg /= count
    return avg

print(list_avg([0, 1, 2, 3, "TTTT"], 2))