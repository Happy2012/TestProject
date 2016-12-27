from random import *
from time import *
import fileinput
from pprint import pprint
date1 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2008, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
random_time = uniform(time1, time2)
print asctime(localtime(random_time))

num = input('How many dice?')
sides = input('How many sides per die?')
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print 'The result is', sum

values = range(1, 11) + 'Jack Queen King'.split()
suits = 'diamonds clubs hearts spades'.split()
deck = ['%s of %s' % (v, s) for v in values for s in suits]
shuffle(deck)
pprint(deck[:12])




