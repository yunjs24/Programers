
def solution(a, b, n):
    answer = 0
    
    while True:
        if n < a:
            break
        answer += n // a * b
        n -= n // a * ( a - b)
    
    return answer
