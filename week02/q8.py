from math import radians


def laps(radius, x1, x2, time):
    pi = 3.14
    cevre = 2 * pi * radius
    total_x1 = time * x1
    total_x2 = time * x2
    laps_x1 = int(total_x1 // cevre)
    laps_x2 = int(total_x2 // cevre)
    
    print(f"First runner = {laps_x1} laps - Second runner = {laps_x2} laps")
    
    
radius = int(input())
x1 = int(input())
x2 = int(input())
time = int(input())
laps(radius, x1, x2, time)