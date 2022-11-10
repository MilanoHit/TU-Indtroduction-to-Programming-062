n = int(input())
nfact = 1
for i in range (0, n):
    nfact *= n - i

print(nfact)