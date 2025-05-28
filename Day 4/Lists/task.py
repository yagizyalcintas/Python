from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'job'])

man = Person(True,50,"c")
print(man)