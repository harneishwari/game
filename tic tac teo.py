import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [" " for _ in range(9)]

def check_winner():
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    if " " not in board:
        messagebox.showinfo("Tic Tac Toe", "It's a draw!")
        window.quit()
    return False
 
def on_click(button_id):
    global current_player

    if board[button_id] == " ":
        board[button_id] = current_player
        buttons[button_id].config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player} wins!")
            window.quit()
        else:
            current_player = "X" if current_player == "O" else "O"


window = tk.Tk()
window.title("Tic Tac Toe")


buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(window, text=" ", width=10, height=2,
                       command=lambda i=i: on_click(i))
    button.grid(row=row, column=col)
    buttons.append(button)

# Run the game
window.mainloop()
