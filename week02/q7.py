def mesafe(x1, y1, x2, y2):
    distance = ((x2-x1) ** 2 + (y2-y1) ** 2 ) ** 0.5
    print("%.2f" % distance)
    
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
mesafe(x1, y1, x2, y2)