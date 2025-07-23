import pyfiglet
def main():
    welcome_text = pyfiglet.figlet_format("welcome :-")
    print(welcome_text)

board = {1:" ", 2:" ", 3:" ",
         4:" ", 5:" ", 6:" ",
         7:" ", 8:" ", 9:" "}

def showBoard():
    print(board[1],"|" , board[2] , "|" , board[3])
    print("--+---+--")
    print(board[4],"|" , board[5] , "|" , board[6])
    print("--+---+--")
    print(board[7],"|" , board[8] , "|" , board[9])
showBoard()

if __name__ == "__main__":
    main()