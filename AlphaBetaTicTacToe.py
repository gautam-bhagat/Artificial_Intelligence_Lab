
def GameBoard(b):

    board = [ b [i:i+3] for i in range(0,9,3) ]

    d ={1:"X",-1:'O',0:'_'}
    for i in range(len(board)):
        for j in range(len(board)):
            print(d[board[i][j]],end=" | ")
        print()
    print()



def getBlanks(board):
    blanks = []
    for i in range(len(board)):
        if board[i] == 0 :
            blanks.append(i)

    return blanks


def isBoardFull(board):
    if len(getBlanks(board)) > 0:
        return False
    return True



def isPlayerWinning(board,player):
    win_cond = [ (0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,5),(2,7,8),
                 (0,4,8),(2,4,6)
               ]

    for state in win_cond:
        if all(board[i] == player for i in state):
            return True
        
    return False



def getScore(board):

    if isPlayerWinning(board,1):
        return 10
    elif isPlayerWinning(board,-1):
        return -10
    else :
        return 0


def alphaBeta(board,depth,alpha,beta,isMaximizing):

    if isPlayerWinning(board,1):
        return (1,None)
    elif isPlayerWinning(board,-1):
        return (-1,None)
    elif isBoardFull(board):
        return (0,None)
    
    if isMaximizing:
        best_score = -10000
        best_move  = None

        for blank in getBlanks(board):
            board[blank] = 1 # 1 represent X. Our AI will be always X
            score , _ = alphaBeta(board,depth-1,alpha,beta,False)
            board[blank] = 0

            if score > best_score:
                best_score = score
                best_move = blank
                alpha =  max(alpha,best_score)

                if beta <= alpha:
                    break

        if best_move == None:
            return (best_score,-1)
        else:
            return (best_score,best_move)
    else :
        best_score = 10000
        best_move  = None

        for blank in getBlanks(board):
            board[blank] = -1 # -1 represent O.User will be always O
            score , _ = alphaBeta(board,depth-1,alpha,beta,True)
            board[blank] = 0

            if score <  best_score:
                best_score = score
                best_move = blank
                beta =  min(beta,best_score)

                if beta <= alpha:
                    break

        if best_move == None:
            return (best_score,-1)
        else:
            return (best_score,best_move)


def aiMove(board):
    _ , best_move = alphaBeta(board,len(getBlanks(board)) , -1000,1000,True)

    if best_move is not None:
        board[best_move] = 1

    return board

def playerMove(board):
    while True:
        p = (int(input("Enter a move from (1-9) : "))-1)
       
        if p in getBlanks(board):
            board[p] = -1
            break
        else:
            print("Try again !!")

    return board

def play():
    board = [0]*9
    print("=================================================")
    print("TIC-TAC-TOE using MINIMAX with ALPHA-BETA Pruning")
    print("=================================================")

    print("You are playing as 'O' and Computer is 'X'")

    while True:
        
        board = playerMove(board)

        if isPlayerWinning(board,-1):
            print("Congrats! You Won!")
            break
        elif isPlayerWinning(board,1):
            print("Sorry! You Lost!")
            break
        elif isBoardFull(board):
            print("OOps! It's a draw.")
            break
        board = aiMove(board)
        GameBoard(board)
        if isPlayerWinning(board,-1):
            print("Congrats! You Won!")
            break
        elif isPlayerWinning(board,1):
            print("Sorry! You Lost!")
            break
        elif isBoardFull(board):
            print("OOps! It's a draw.")
            break


play()