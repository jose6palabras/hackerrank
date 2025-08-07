#problem number 2 practice test challenge Turing
#valid parentheses
def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {')': '(', ']': '[', '}': '{'}
    for c in s:
      if c in closeToOpen.keys():
        if not stack or stack.pop() != closeToOpen[c]:
          return False
      else:
        stack.append(c)
  
    return True if not stack else False

if __name__ == "__main__":
    line = input()
    if isValid(line):
        print("valid")
    else:
        print("invalid")