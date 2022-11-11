import sys

lines = []
file_len = int(input())

for line in sys.stdin:
    lines.append(line)
    if len(lines) == file_len:
        break

allValid = True
errorCodes = []
for line in lines:
    line = line.rstrip('\n')
    output = line.split(' ')[1]
    valid = True
    if output.lower() == 'true':
        valid = True
    elif output.lower() == 'false':
        valid = False
    if not valid:
        allValid = False
    if not valid:
        errorCodes.append(line.split(' ')[2])

if allValid:
    print("Yes")
else:
    print("No")
    print(' '.join(errorCodes))

