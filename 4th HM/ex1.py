n = int(input())
arr = []
for i in range(0, n):
    p = int(input())
    arr.append(p)
k = int(input("Enter 0 or 1:"))

if k == 0:
    for i in range(0, n):
        if i % 2 == 0:
            arr[i] += 5
elif k == 1:
    for i in range(0, n):
        if i % 2 == 1:
            arr[i] += 10

print(arr)