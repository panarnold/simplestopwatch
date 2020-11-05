#! python
# simplestopwatch.py - very simple stopwatch, absolutely for free
# XI 2020 Arnold Cytrowski



import time

print('Press <ENTER> to start. Press <ENTER> again for starting new lap')
print('Press <CTRL + C> for finish the program')
input()
print('Start!')
start_time = time.time()
last_time = start_time
lap_num = 1

try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print(f'Lap#{lap_num}: total time:{total_time}, laptime:{lap_time}', end='')

        lap_num += 1
        last_time = time.time()
except KeyboardInterrupt:
    print('And it\'s done')