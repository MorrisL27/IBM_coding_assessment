import sys


def convert(original_size):
    size = original_size.upper()
    value = 0
    if len(size) == 1:
        if size == 'S':
            value = 1
        elif size == 'M':
            value = 2
        elif size == 'L':
            value = 3
    else:
        letter = size[-1]
        if letter == 'S':
            value = 1 - (len(size) - 1)
        elif letter == 'M':
            value = 2
        elif letter == 'L':
            value = 3 + (len(size) - 1)
    return value


lines = []
for line in sys.stdin:
    lines.append(line)
    if len(lines) == 4:
        break

num_size = int(lines[0].rstrip('\n'))
sizes = lines[1].rstrip('\n').split(' ')
num_req = int(lines[2].rstrip('\n'))
reqs = lines[3].rstrip('\n').split(' ')

if num_size < num_req:
    print('No')
else:
    size_values = []
    for size in sizes:
        size_values.append(convert(size))
    req_values = []
    for req in reqs:
        req_values.append(convert(req))

    size_values = sorted(size_values, reverse=True)
    req_values = sorted(req_values, reverse=True)
    result = True
    for i in range(len(req_values)):
        if size_values[i] < req_values[i]:
            result = False
    if result:
        print('Yes')
    else:
        print('No')

