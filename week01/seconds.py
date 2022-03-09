year = int(input())
month = int(input())
day = int(input())
hour = int(input())
minute = int(input())

month = month + 12 * year
day = day + 30 * month + year * 5
hour = hour + 24 * day
minute = minute + 60 * hour
minute *= 60
print(minute)