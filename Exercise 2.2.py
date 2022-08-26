import math

print("Hello, Aaban")

radius_str = input('Pick a length to be the radius of a circle: ')
radius = float(radius_str)
circular_area = (radius * radius * math.pi)
print(f"{circular_area:2.3f}")
