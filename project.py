import pyfiglet

def message():
    welcome_text = pyfiglet.figlet_format("welcome to Tic Tac Toe Game")
    print(welcome_text)

def main():
    message()
    board = {
        1:" ", 2:" ", 3:" ",
        4:" ", 5:" ", 6:" ",
        7:" ", 8:" ", 9:" "
    }
    Show_Board(board)

    player1 = "X"
    player2 = "O"

    while True:
        print(player1 , "chance")
        position = int(input("Enter position (1-9): "))
        insert(player1 , position, board)
        
        print(player2 , "chance")
        position = int(input("Enter position (1-9): "))
        insert(player2 , position, board)


def Show_Board(board):
    print()
    print(board[1],"|" , board[2] , "|" , board[3])
    print("--+---+--")
    print(board[4],"|" , board[5] , "|" , board[6])
    print("--+---+--")
    print(board[7],"|" , board[8] , "|" , board[9])
    print()

def Check_For_Draw(board):
    for i in board.values():
        if i == " ":
            return False
    return True

def Check_For_Win(player, board):
    # Row conditions
    if board[1] == board[2] and board[1] == board[3] and board[1] == player:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == player:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == player:
        return True

    # column conditions
    elif board[1] == board[4] and board[1] == board[7] and board[1] == player:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == player:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == player:
        return True

    # Diagonal conditions
    elif board[1] == board[5] and board[1] == board[9] and board[1] == player:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == player:
        return True
    else:
         return False

def insert(player , position, board):
    if board[position] == " ":
        board[position] = player
        Show_Board(board)
        if Check_For_Win(player, board):
            print(player , "is winner.")
            quit()
        if Check_For_Draw(board):
            print("Game Draw.")
            quit()
    else:
        print("space already occupied.")
        position = int(input("Enter new position: "))
        insert(player , position, board)



if __name__ == "__main__":
    main()