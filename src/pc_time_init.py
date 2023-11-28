# initialize clock time from pc before loading to pico device

import datetime

now = datetime.datetime.now()
formatted_time = now.strftime("%Y, %m, %d, %w, %H, %M, %S")
print(formatted_time)
