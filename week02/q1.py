#print("%.2f" % 5)
#x = 5.4153134538
#print("%.3f" % x)
x = float(input())
y = float(input())

per_x = ((x) / (x + y)) * 100
per_y = ((y) / (x + y)) * 100
per_x = "%.2f" % per_x
per_y = "%.2f" % per_y
print(per_x + "% "+ per_y + "%")