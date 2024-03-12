def calPoints(ops):
    val = []
    for i in range(len(ops)):
        if ops[i] in ['D', 'C', '+']:
            if ops[i] == 'D':
                val.append(val[-1]*2)
            elif ops[i] == 'C':
                val.pop(-1)
            else:
                val.append(val[-1]+val[-2])
        else:
            val.append(int(ops[i]))
    print(val)
    return sum(val)
if __name__ == '__main__':
    line = input()
    ops = line.strip().split()
    print(calPoints(ops))