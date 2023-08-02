# bounce.py
#
# Exercise 1.5
building_height = 100
actual_height = 0
i = 0

while i < 10:
    building_height = round(building_height * 3 / 5, 4)
    print(building_height)
    i += 1
