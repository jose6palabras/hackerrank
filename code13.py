# A Python program to demonstrate working of OrderedDict
from collections import OrderedDict

print("This is a Dict:\n")
d = {}
d['a'] = 1
d['c'] = 3
d['b'] = 2
d['d'] = 4

for key, value in d.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)

print("\nThis is a dictionary of Jurassic Park/World movies:\n")
jurassic_movies = OrderedDict()
jurassic_movies['Jurassic Park'] = 1993
jurassic_movies['The Lost World: Jurassic Park'] = 1997
jurassic_movies['Jurassic Park III'] = 2001
jurassic_movies['Jurassic World'] = 2015
jurassic_movies['Jurassic World: Fallen Kingdom'] = 2018
jurassic_movies['Jurassic World: Dominion'] = 2022

for key, value in jurassic_movies.items():
    print(key, value)
