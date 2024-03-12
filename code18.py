def isValid(line):
    opend = ['(', '[', '{']
    closed = [')', ']', '}']
    if line[0] in closed:
        return False
    else:
        for i in range(len(line)):
            if line[i] in opend:
                4
        



if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("is valid")
    else:
        print("invalid")