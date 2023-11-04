from itertools import combinations
n = int(input())
n_list = input().split()
k = int(input())
comb = list(combinations(n_list, k))
counter = 0
for i in comb:
    if 'a' in i:
        counter += 1
pr = counter/len(comb)
print("%.3f" % pr)