arr = []

n = int(input())

while n != 0:
    arr.append(n % 10)
    n //= 10


im2 = tuple(arr)
im1 = tuple(arr[::-1])


print(im1)
print(im2)
