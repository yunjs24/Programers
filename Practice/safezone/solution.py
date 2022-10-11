
dir = [(0,1), (0,-1), (1,-1), (1,0), (1,1), (-1,-1), (-1,0), (-1, 1)]

def safe(p, board, n):
    x, y = p
    if board[x][y] == 1:
        return False
    for d in dir:
        r, c = tuple(sum(e) for e in zip(d,p))
        if r < 0 or c < 0 or r >= n or c >= n:
            continue
        if board[r][c] == 1:
            return False
    return True

def solution(board):
    answer = 0
    n = len(board)
    
    for r in board:
        print(r)
    
    for i, r in enumerate(board):
        for j, c in enumerate(r):
            if safe((i,j), board, n):
                answer+=1
    return answer
