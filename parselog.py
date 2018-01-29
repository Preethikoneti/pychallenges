import re
file = open("/Users/kbeattie/Desktop/messages.log", "r")
lines = file.readlines()

last_minute = 0
running_count = 0
for line in lines:
    minute = re.match(r'^(\w+ \d+ \d+\:\d+).+$', line).groups()[0]
    print minute
    # if minute == last_minute:
    #     running_count += 1
    # elif:
    #     minute_count = 0
        
# for minute in minute_count:
#     print  minute + ',' + minute_count[minute]