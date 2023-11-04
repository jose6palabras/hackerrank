n, module = map(int, input().split())
k_dicc = {}
for i in range(n):
    k_dicc[i] = list(map(int, input().split()))
    k_dicc[i].pop(0)
def s(array):
    maxValue = 0
    for i in array:
        fx = i**2
        if fx%module > maxValue:
            maxValue = fx%module
    return maxValue
sum = 0
for i in k_dicc:
    sum = sum + s(k_dicc[i])
print(sum)