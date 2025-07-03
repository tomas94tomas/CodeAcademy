import math

def area_of_circle(radius):
    return math.pi * (radius ** 2)

radii = [1, 2.5, 5, 10]

for r in radii:
    area = area_of_circle(r)
    print(f"Radius: {r} | Area: {area:.2f}")