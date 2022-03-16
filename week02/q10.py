def passer_rating(comp, attempts, yards, td, i):
    C = ((comp / attempts) * 100 -30) / 20
    Y = ((yards / attempts) - 3) / 4
    T = (td / attempts) * 20
    I = 2.375 - ((i / attempts) * 35)
    
    passer_rating_result = ((C+Y+T+I)/6) * 100
    return "%.2f" % passer_rating_result


comp = int(input())
attempts = int(input()) 
yards = int(input())
td = int(input())
i = int(input())
print(passer_rating(comp, attempts, yards, td, i))