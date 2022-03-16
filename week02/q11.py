#current_population = 84500000
#def population(year):
#    global current_population
#    current_year = 2022
#    
#    total_year = year - current_year
#    total_seconds = total_year * 365 * 24 * 60 * 60
#    total_birth = total_seconds / 15
#    total_death = total_seconds / 20
#    total_death *= -1
#    total_suris = total_seconds / 100
#    current_population += total_birth + total_death + total_suris
#    current_population = int(current_population)
#population(2050)
#print(current_population)


def population(year):
    current_population = 84500000
    current_year = 2022
    
    total_year = year - current_year
    total_seconds = total_year * 365 * 24 * 60 * 60
    total_birth = total_seconds / 15
    total_death = total_seconds / 20
    total_death *= -1
    total_suris = total_seconds / 100
    current_population += total_birth + total_death + total_suris
    current_population = int(current_population)
    print(current_population)

year = int(input())
population(year)

