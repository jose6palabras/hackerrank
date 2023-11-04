n,m = map(int,input().split())
N = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
C = A | B
Nn = (i for i in N if i in C)
print(sum(1 if i in A else -1 for i in Nn ))