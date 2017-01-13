import re
file = open("/Users/kbeattie/Desktop/messages.log", "r")
data = file.readlines()
results = []
matches = []
last_interval = 0
running_count = 1

i = 0
for line in data:
    interval = re.findall(r'^(\s\w+\s\d+\s\d+\:\d+)', line)
    if len(interval) == 1:
        if interval == last_interval:
            running_count += 1
            previous_count = running_count - 1
            del results[-1]
            matches = [str(interval), str(running_count)]
        else:
            running_count = 1
            matches = [str(interval), str(running_count)]
        last_interval = interval
        results.append((matches, running_count))
        i = i + 1

for event in results:
    print event[0]