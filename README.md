# **CS50P-Project:- Tic Tac Toe**    
my final project for the CS50P Python course.        
Video Demo:  <URL HERE>        
### Description:     
The Tic Tac Toe Game is a classic two-player game implemented using Python in a simple text-based/console interface. The goal of the game is to provide an interactive experience for two users who take turns to place their symbols (X or O) on a 3×3 grid.

The game is built to handle player input, check for valid moves, and determine the game result (win, loss, or draw) based on the current state of the board.

🔧 Game Rules
The game is played on a 3x3 grid.
Two players take turns — Player 1 is X, and Player 2 is O.
A player wins if they manage to place three of their marks in a horizontal, vertical, or diagonal row.
If all 9 cells are filled without a winner, the game ends in a draw.

### ✅ Features

Interactive command-line interface
Two-player mode (local multiplayer)
Turn-based gameplay with alternating players
Automatic win or draw detection
Board display updates after each turn
Input validation to handle:
Non-numeric input
Out-of-range input
Occupied cells

### 📁 Project Structure

bash  
Copy  
Edit  
tic_tac_toe/  
**1.**project.py             # Main Python script containing the game logic
**2.**README.md              # Project overview and usage instructions
**3.**requirements.txt       # (Optional) if you add GUI or other libraries

### 🧠 How It Works

Game Board Representation:
The game board is represented using a list of 9 elements (or a 3x3 nested list).
Empty spaces are initially numbered 1 to 9 for easy reference.
Player Input:
Players are prompted to enter the position where they want to place their mark.
The input is checked for validity before updating the board.
**1.****Move Validation:
The program checks if the input is a number between 1–9 and whether the chosen cell is empty.
**2.**Win Checking Logic:
After each move, the game checks all possible winning combinations (rows, columns, diagonals).
**3.**Draw Condition:
If the board is full and no winner is detected, the game declares a draw.

### ✅ Libraries Used (Console Version)

Library	Purpose: Built-in is Used for input/output, loops, logic

### ✅ Standard Python Features Used:

print() – to display the game board  
input() – to take user input  
int() – to convert string input to integers  
list – to represent the game board  
if/else, while, for – for control flow and logic  


