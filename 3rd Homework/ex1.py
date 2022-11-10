n = int(input())

a = 0
b = 1
print(a)
print(b)
for i in range(0, n):
    print(a + b)
    c = b
    b = a + b
    a = c
