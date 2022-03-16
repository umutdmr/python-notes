#print("a", end="\n\n")
#print(5)
def floor(number):
    return number % int(number)
    
    
    
x = float(input())
y = float(input())
z = float(input())
x = "%.2f" % floor(x)
y = "%.2f" % floor(y)
z = "%.2f" % floor(z)
print(x,y,z)