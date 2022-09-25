# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    zeros = 0
    cnt = 0
    for i in range(6):
        if lottos[i] == 0:
            zeros += 1
        elif lottos[i] in  win_nums:
           cnt += 1
    if zeros == 6:
        return [1, 6]
    if cnt == 0 and zeros == 0:
        return [6, 6]
    answer = [7 - cnt, 7 - cnt - zeros]
        
    return sorted(answer)
