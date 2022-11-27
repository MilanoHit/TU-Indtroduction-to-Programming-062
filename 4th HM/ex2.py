dict = {}

arr = []

n = int(input())

for i in range(0, n):
    key = input()
    value = input()
    dict[key] = value

m = int(input())

for i in range(m):
    kek = input()
    arr.append(kek)

for i in range(len(arr)):
    if arr[i] in dict.keys():
        key = arr[i]
        arr[i] = dict[arr[i]]
        dict.pop(key)

print(dict)
print(arr)