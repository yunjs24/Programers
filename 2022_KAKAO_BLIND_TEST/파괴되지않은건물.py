
def solution(board, skill):
    w, h = len(board), len(board[0])
    
    for s in skill:
        doSome(board, s[0], s[5], s[1:3], s[3:5])

    answer = 0
    for r in board:
        for v in r:
            if v > 0:
                answer += 1
    return answer

def doSome(board, option, degree, p1, p2):
    # print(f'v : {p1}')
    r1, c1 = p1[0], p1[1]
    r2, c2 = p2[0], p2[1]
    if option == 1:
        degree *= -1
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            board[i][j] += degree
    