# Python Program for Tic-Tac-Toe Game

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize board
board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
turn = 0

def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return board[1][1]
    return None

def on_click(row, col, button):
    global turn
    if board[row][col] == " ":
        board[row][col] = players[turn]
        button.config(text=players[turn])
        winner = check_winner()
        if winner:
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            root.quit()
        turn = 1 - turn

# Create buttons
buttons = [[tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                      command=lambda r=i, c=j: on_click(r, c, buttons[r][c]))
            for j in range(3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j].grid(row=i, column=j)

root.mainloop()