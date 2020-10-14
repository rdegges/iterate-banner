from sys import stdout
from time import sleep

intro = open('banner').read()

for c in intro:
    stdout.write(c)
    stdout.flush()

    t = 0.08
    if c.isspace() or c == '=':
        t = 0
    elif not c.isalpha():
        t = 0.01

    sleep(t)


