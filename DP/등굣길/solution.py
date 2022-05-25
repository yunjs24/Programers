def solution(m, n, puddles):
    answer = 0
    field = [[0]*(m+1) for i in range(n+1)]
    for (j,i) in puddles:
        field[i][j] = -1
    
    if m > 1 and field[1][2] != -1:
        field[1][2] = 1
    if n > 1 and field[2][1] != -1:
        field[2][1] = 1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if field[i][j] != -1:
                if i == n and j == m:
                    answer = field[i][j]
                elif j == m and i < n:
                    if field[i+1][j] != -1:
                        field[i+1][j] += field[i][j]
                elif i == n and j < m:
                    if field[i][j+1] != -1:
                        field[i][j+1] += field[i][j]
                else :
                    if field[i][j+1] != -1:
                        field[i][j+1] += field[i][j]
                    if field[i+1][j] != -1:
                        field[i+1][j] += field[i][j]

    return answer%1000000007