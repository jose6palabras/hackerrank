from collections import deque
n_inp = int(input())
for i in range(0, n_inp):
    lena = input()
    deque_array = deque(list(map(int, input().split())))
    pile = True
    max_n = float('inf')
    while deque_array:
        if max_n >= deque_array[0] >= deque_array[-1]:
            max_n = deque_array[0]
            deque_array.popleft()
        elif max_n >= deque_array[-1] >= deque_array[0]:
            max_n = deque_array[-1]
            deque_array.pop()
        else:
            print("No")
            pile = False
            break
    if pile:
        print("Yes")