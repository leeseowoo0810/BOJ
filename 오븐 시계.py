hour, minute = map(int, input().split())
time = int(input())

if minute + time >= 60:
    hour += (minute + time) // 60
    minute += time - 60 * ((minute + time) // 60)
    if hour >= 24:
        hour -= 24
else:
    minute += time

print(hour, minute)