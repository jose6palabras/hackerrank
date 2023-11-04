from itertools import product
n, module = map(int, input().split())
l=[]
for i in range(n):
    x_l = list(((int(i)%module)**2)%module for i in input().split())
    x_l.pop(0)
    l.append(x_l)
p = list(product(*l))
max_value = 0
for n in p:
    suma = sum(n)%module
    if suma > max_value:
        max_value = suma
print(max_value)
