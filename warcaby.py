white_tile = "▓"
black_tile = "░"

w, h = 8, 8
board = [[0 for x in range(w)] for y in range(h)] 

for i in range(0,8,2):
    for j in range(0,8):
        if (i*8 + j) % 2 == 0:
            board[i][j] = white_tile
            board[i+1][j] = black_tile
        else:
            board[i][j] = black_tile
            board[i+1][j] = white_tile

def print_board():
    print(" ABCDEFGH ")
    for i in range(0,8):
        print(8-i,end="")
        for j in range(0,8):
            print(board[i][j],end="")
        print(8-i)
    print(" ABCDEFGH ")

def set_pawns():
    board[7][0] = "w"
    board[7][2] = "w"
    board[7][4] = "w"
    board[7][6] = "w"
    
    board[6][1] = "w"
    board[6][3] = "w"
    board[6][5] = "w"
    board[6][7] = "w"

    board[5][0] = "w"
    board[5][2] = "w"
    board[5][4] = "w"
    board[5][6] = "w"

    board[2][1] = "b"
    board[2][3] = "b"
    board[2][5] = "b"
    board[2][7] = "b"

    board[1][0] = "b"
    board[1][2] = "b"
    board[1][4] = "b"
    board[1][6] = "b"

    board[0][1] = "b"
    board[0][3] = "b"
    board[0][5] = "b"
    board[0][7] = "b"

def convert_notation(chess):
    match chess[0]:
        case "a":
            y_index = 0
        case "b":
            y_index = 1
        case "c":
            y_index = 2
        case "d":
            y_index = 3
        case "e":
            y_index = 4
        case "f":
            y_index = 5
        case "g":
            y_index = 6
        case "h":
            y_index = 7
        case _:
            y_index = -1

    match chess[1]:
        case "1":
            x_index = 7
        case "2":
            x_index = 6
        case "3":
            x_index = 5
        case "4":
            x_index = 4
        case "5":
            x_index = 3
        case "6":
            x_index = 2
        case "7":
            x_index = 1
        case "8":
            x_index = 0
        case _:
            x_index = -1

    return x_index, y_index

def check_endgame():
    if (sum(x.count("b") for x in board)) == 0 and (sum(x.count("B") for x in board)) == 0:
        print("-------------------")
        print("ZWYCIĘSTWO CZARNYCH")
        print("-------------------")
        exit()
    elif (sum(x.count("w") for x in board)) == 0 and (sum(x.count("W") for x in board)) == 0:
        print("------------------")
        print("ZWYCIĘSTWO BIAŁYCH")
        print("------------------")
        exit()

def help():
    print("-"*10)
    print("Ruchy piszemy w następujący sposób:")
    print("d4e5")
    print("Co oznacza - pionek z d4 na e5")
    print("-"*10)

def promotion(color, x):
    if color == "b" and x == 7: return True
    elif color == "w" and x == 0: return True
    else: return False;

def queen_move(move, color):
    from_x, from_y = convert_notation(move[0]+move[1])
    to_x, to_y = convert_notation(move[2]+move[3])

    if from_x not in range(0,8) or from_y not in range(0,8) or to_x not in range(0,8)  or to_y not in range(0,8): #poza zakres
        print("Nieprawidłowy ruch! - poza zakresem")
        return False

    if color == "w":
        if abs(from_x - to_x) == 2 and abs(from_y - to_y) == 2: #do przodu/tylu o 2 na skos o 2 (bicie)
                if from_y != 0 and from_y != 7:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["b","B"]) or (board[(from_x + to_x)//2][from_y - 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True
                elif from_y == 0:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True
                elif from_y == 7:
                    if(board[(from_x + to_x)//2][from_y - 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True

    elif color == "b":
        if abs(from_x - to_x) == 2 and abs(from_y - to_y) == 2: #do przodu/tylu o 2 na skos o 2 (bicie)
            if from_y != 0 and from_y != 7:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["w","W"]) or (board[(from_x + to_x)//2][from_y - 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True
            elif from_y == 0:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True
            elif from_y == 7:
                    if(board[(from_x + to_x)//2][from_y - 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        return True

    if abs(from_x - to_x) != 1: #do przodu/tylu
        print("Nieprawidłowy ruch! - za dużo do przodu")
        return False

    if abs(from_y - to_y) != 1: #na skos
        print("Nieprawidłowy ruch! - za dużo na skos")
        return False

    if board[to_x][to_y] in ["b","w","B","W","▓"]: #zajęte pole
        print("Nieprawidłowy ruch! - nieprawidłowe pole")
        return False

    return True


def white_move():
    while True:
        move = input("Ruch białych: ")

        from_x, from_y = convert_notation(move[0]+move[1])
        to_x, to_y = convert_notation(move[2]+move[3])

        pawn = board[from_x][from_y]

        if pawn in ["b","B","░"]:
            print("Nieprawidłowy ruch! - zły kolor")
            continue

        if pawn == "w":

            if from_x not in range(0,8) or from_y not in range(0,8) or to_x not in range(0,8)  or to_y not in range(0,8): #poza zakres
                print("Nieprawidłowy ruch! - poza zakresem")
                continue
            if (from_x - to_x) == 2 and abs(from_y - to_y) == 2: #do przodu o 2 na skos o 2 (bicie)
                if from_y != 0 and from_y != 7:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["b","B"]) or (board[(from_x + to_x)//2][from_y - 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        break
                elif from_y == 0:
                    if(board[(from_x + to_x)//2][from_y + 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        break
                elif from_y == 7:
                    if(board[(from_x + to_x)//2][from_y - 1] in ["b","B"]): #do przodu o jedno i na skos o jedno zajete przez b
                        board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                        break
            if (from_x - to_x) != 1: #do przodu
                print("Nieprawidłowy ruch! - za dużo do przodu")
                continue
            if abs(from_y - to_y) != 1: #na skos
                print("Nieprawidłowy ruch! - za dużo na skos")
                continue
            if board[to_x][to_y] in ["b","w","B","W","▓"]: #zajęte pole
                print("Nieprawidłowy ruch! - nieprawidłowe pole")
                continue

        else:
            if queen_move(move,"w") == False: continue

        break

    if promotion("w",to_x) and pawn == "w": pawn = "W"

    board[from_x][from_y] = black_tile
    board[to_x][to_y] = pawn
    check_endgame()
    

def black_move():
    while True:
        move = input("Ruch czarnych: ")

        from_x, from_y = convert_notation(move[0]+move[1])
        to_x, to_y = convert_notation(move[2]+move[3])

        pawn = board[from_x][from_y]

        if pawn in ["w","W","░"]:
            print("Nieprawidłowy ruch! - zły kolor")
            continue

        if board[from_x][from_y] == "b":

            if from_x not in range(0,8) or from_y not in range(0,8) or to_x not in range(0,8)  or to_y not in range(0,8): #poza zakres
                print("Nieprawidłowy ruch! - poza zakresem")
                continue
            if (to_x - from_x) == 2 and abs(from_y - to_y) == 2: #do przodu o 2 na skos o 2 (bicie)

                if from_y != 0 and from_y != 7:
                        if(board[(from_x + to_x)//2][from_y + 1] in ["w","W"]) or (board[(from_x + to_x)//2][from_y - 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                            board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                            break
                elif from_y == 0:
                        if(board[(from_x + to_x)//2][from_y + 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                            board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                            break
                elif from_y == 7:
                        if(board[(from_x + to_x)//2][from_y - 1] in ["w","W"]): #do przodu o jedno i na skos o jedno zajete przez b
                            board[(from_x + to_x)//2][(from_y + to_y)//2] = black_tile
                            break

            if (to_x - from_x) != 1: #do przodu
                print("Nieprawidłowy ruch! - za dużo do przodu")
                continue
            if abs(from_y - to_y) != 1: #na skos
                print("Nieprawidłowy ruch! - za dużo na skos")
                continue
            if board[to_x][to_y] in ["b","w","B","W","▓"]: #zajęte pole
                print("Nieprawidłowy ruch! - nieprawidłowe pole")
                continue

        else:
            if queen_move(move,"b") == False: continue

        break

    if promotion("b",to_x) and pawn == "b": pawn = "B"

    board[from_x][from_y] = black_tile
    board[to_x][to_y] = pawn
    check_endgame()

help()
set_pawns()
print_board()
while True:
    white_move()
    print_board()
    black_move()
    print_board()
