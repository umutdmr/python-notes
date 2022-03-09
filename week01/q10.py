x = int(input())
y = int(input())
z = int(input())

result = 0

if(x % 2 == 1):
    result += x
    
if(y % 2 == 1):
    result += y
    
if(z % 2 == 1):
    result += z
    

print(result)
