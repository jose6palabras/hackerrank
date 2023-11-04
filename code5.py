from collections import deque
n_inp = int(input())
for i in range(0, n_inp):
    lena = input()
    deque_array = deque(list(map(int, input().split())))
    pile = True
    while deque_array:
        num_max = max(deque_array)
        if deque_array[0] == num_max:
            deque_array.popleft()
        elif deque_array[-1] == num_max:
            deque_array.pop()
        else:
            print("No")
            pile = False
            break
    if pile:
        print("Yes")