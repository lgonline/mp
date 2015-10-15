__author__ = 'Administrator'

lists = [x * x for x in range(11)]
print(lists)

generators = (x*x for x in range(11))
for g in generators:
    print(g)