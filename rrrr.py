import weakref

s1 = {1, 2, 3}
s2 = s1


def bye():
    print('Żegnam...')

ender = weakref.finalize(s1, bye)

ender.alive

s2 = 'Tomek'

