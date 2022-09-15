def solution(s):
    top = 0
    for c in s:
        if c == '(':
            top +=1
        elif c == ')':
            top -= 1
        if top < 0:
            return False
    if top == 0:
        return True
    
    return False
