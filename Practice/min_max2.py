def solution(s):
    answer = list(map(int, s.split()))
    return str f'{min(answer)} {max(answer)}'
