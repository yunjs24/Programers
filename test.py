# import math

# def solution(levels):
#     answer = 0
#     N = len(levels)
#     if N < 3:
#         return -1
#     print(levels[math.ceil(N * 0.75)])
    
# solution([1,2,3,4,4,4])

import math

def solution(levels):
    answer = 0
    levels = levels.sort()
    N = len(levels)
    if N < 3:
        return -1
    flag = math.ceil(N * 0.75)
    if flag + 1 < N:
        if levels[flag] == levels[flag + 1]:
            return -1
    return levels[flag]

print(solution(list(range(1,2147483637))))


# from itertools import permutations

# def isEnough(now, demand):
#     if now >= demand:
#         return 1
#     return 0

# def solution(k, dungeons):
#     answer = -1
#     now = k

#     for case in permutations(list(range(0, len(dungeons)))):
#         now = k
#         for i in case:
#             if isEnough(k, dungeons[i][0]):
#                 now -= dungeons[i][1]

#     return answer

# solution(80, [[80,20],[50,40],[30,10]])