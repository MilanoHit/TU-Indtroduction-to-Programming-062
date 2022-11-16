n = int(input())
arr = []
dict = {}
for i in range(1, n + 1):
    arr.append(i)

for i in range(0, len(arr)):
    dict.update({arr[i] : arr[-i - 1]})
print(dict)