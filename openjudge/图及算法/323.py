def dfs(n, k, board):
    blanks = sum(row.count('#') for row in board)
    num = 0
    row_visited = [False] * n
    col_visited = [False] * n
    def recur(row, placed):
        nonlocal num, row_visited, col_visited, board
        if placed == k:
            num += 1
            return
        if row >= n or n - row < k - placed:
            return
        
        recur(row + 1, placed)
        for col in range(n):
            if board[row][col] == '#' and not row_visited[row] and not col_visited[col]:
                row_visited[row] = True
                col_visited[col] = True
                recur(row + 1, placed + 1)
                row_visited[row] = False
                col_visited[col] = False
    recur(0, 0)
    return num

ans = []
while True:
    n, k = list(map(int, input().split()))
    if n == -1 and k == -1:
        break
    board = []
    for _ in range(n):
        board.append(input().strip())
    blanks = sum(row.count('#') for row in board)
    if blanks < k:
        ans.append(0)
        continue

    ans.append(dfs(n, k, board))

for i in ans:  
    print(i)