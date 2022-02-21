N = int(input())
best_snowball = 0
best_snow = 0
best_time = 0
best_quality = 0
for x in range (1, N + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball = (snowball_snow / snowball_time)**snowball_quality
    if best_snowball < snowball:
        best_snowball = snowball
        best_snow = snowball_snow
        best_time = snowball_time
        best_quality = snowball_quality
print (f'{best_snow} : {best_time} = {int(best_snowball)} ({best_quality})')



