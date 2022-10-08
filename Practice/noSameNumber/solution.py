def solution(arr):
    answer = []
    prev = -1
    for v in arr:
        if prev != v:
            answer.append(v)
            prev = v
    return answer
