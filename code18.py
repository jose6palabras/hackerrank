#problem number 2 
def isValid(line):
    closeToOpend = {')': '(', ']':'[', '}': '{'}
    opened = []
    for p in line:
        if p in closeToOpend.values():
            opened.append(p)
        elif p in closeToOpend.keys():
            if opened and closeToOpend[p] == opened[-1]:
                opened.pop()
            else:
                break
        else:
            break
    return True if not opened else False

if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")