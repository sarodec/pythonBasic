import time

count_seconds = int(input("count down number of seconds: "))

for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end=' ', flush = True)
        time.sleep(1)
    else:
        print('Start')