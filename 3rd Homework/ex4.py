n = int(input())
total = 0
back = 0
for i in range(0, n):
    total += n*10**i + back
    back = n*10**i + back
print(total)