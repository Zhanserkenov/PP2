import math

def vol(radius):
    return (4 / 3) * math.pi * radius ** 3

r = int(input())
print(vol(r))