
board = [["_" for i in range(8)] for i in range(8)]

def ini():
    board[3][4] = "●"
    board[4][3] = "●"
    board[3][3] = "○"
    board[4][4] = "○"

def show(board):
    for item in board:
        print(item)


def put(i, j , n):
    if(board[i][j]=="●"or board[i][j]=="○"):
        return "E"
    if(n==1):
        board[i][j] = "●"
    else:
        board[i][j] = "○"
    return

ini()
show(board)
put(2,3,1)
print("---------------")
show(board)