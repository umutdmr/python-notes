def division(num, div):
    quotient = num // div
    remainder = num % div
    print(f"quotient = {quotient} remainder = {remainder}")

num = int(input())
div = int(input())
division(num, div)