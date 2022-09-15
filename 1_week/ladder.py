import sys

height = int(sys.argv[1])
i = 1
while i <= height:
    print((height - i) * " " + i * "#")
    i += 1
