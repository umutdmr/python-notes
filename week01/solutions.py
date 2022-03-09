#1.a
x = 5
y = 3
print(x)
print(y)
#end and sep parameters...

#1.b
x = 5
y = 3
print(x)
print(y)
#what if we did not use int() outside the input()?

#1.c
x = int(input())
y = int(input())
print(x+y, x-y, x*y, x**y, x%y)
#introduce the mathematical operations

#2.a
x = 5
y = 1.7
z = "I am a string!"
print(type(x))
print(type(y))
print(type(z))
#what is the type of 'a'?

#2.b
x = int(input())
y = float(input())
z = input()
print(x, y, z)
#what if we want to print them line by line in one print function?

#3
x = int(input())
y = int(input())
z = int(input())
sum = x + y + z
print(sum, sum/3, x * y * z) 
#variable declaration

#4
A = int(input())
i = int(input())
n = int(input())
# print(A * (1 + (i / 100)) ** n)
print('%.2f' % (A * (1 + (i / 100)) ** n))
#formatting, fstrings

#5
print(int('6') + int('4'))
print('1' + '4')
print(int(3.9))
print(str(5.3) + '2.7')
print(int('5') * str(0.6))
print(float('3' + '8.6'))
print(3.5 + 6.7)
print(2 ** 3 ** 2 / 32)
print(str(4.4) + str(7.3))
print(int(6.5) + float('6.5'))
print(int(4.5 + 3.2))
print(int(3.2) + int(float(str(3.2))))
#guess the results

#6
years = int(input())
months = int(input())
days = int(input()) 
hours = int(input())
minutes = int(input())

total_days = years * 365 + month * 30 + days
total_hours = total_days * 24 + hours
total_minutes = total_hours * 60 + minutes
print(total_minutes * 60)

#7
# as a program
# money = int(input())
# print('5tl banknotes:', money / 5)
# print('1tl banknotes:', money % 5)
# with functions
def to_banknotes(money):
    print('5tl banknotes:', money / 5)
    print('1tl banknotes:', money % 5)

to_banknotes(57)
to_banknotes(269)

#8
def volume(radius):
    return 4 / 3 * radius ** 3 * 3

print(volume(3))
result = volume(6)
print(result)

#9
def power(number, n):
    return number ** n

print(power(5, 2))
print(power(3, 2))

#10
a = int(input())
b = int(input())
c = int(input())

print(a * (a % 2) + b * (b % 2) + c * (c % 2))

#11
def is_square(number):
    sqroot = number ** 0.5
    sqroot_int = int(sqroot)
    return number == sqroot_int ** 2

print(is_square(23))
print(is_square(25))