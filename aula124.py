# count é um iterador sem fim (itertools)
from itertools import count

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('C1', hasattr(c1, '__iter__'))
print('C1', hasattr(c1, '__next__'))
print('R1', hasattr(r1, '__iter__'))
print('R1', hasattr(r1, '__next__'))
print()
print('Count')
for i in c1:
    if i >= 100:
        break
    print(i)

print()
print('Range')
for i in r1:
    print(i)
