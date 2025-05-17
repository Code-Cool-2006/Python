import tkinter as tk
import random

# Create main window
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("400x500")

# Choices
choices = ["Rock", "Paper", "Scissors"]

def play(choice):
    user_choice.set(choice)
    comp_choice.set(random.choice(choices))
    
    if user_choice.get() == comp_choice.get():
        result.set("It's a Tie!")
    elif (user_choice.get() == "Rock" and comp_choice.get() == "Scissors") or \
         (user_choice.get() == "Paper" and comp_choice.get() == "Rock") or \
         (user_choice.get() == "Scissors" and comp_choice.get() == "Paper"):
        result.set("You Win!")
    else:
        result.set("Computer Wins!")

# Variables
user_choice = tk.StringVar()
comp_choice = tk.StringVar()
result = tk.StringVar()

# UI Elements
tk.Label(window, text="Rock Paper Scissors", font=("Arial", 16)).pack(pady=10)
tk.Label(window, text="Your Choice:").pack()
tk.Label(window, textvariable=user_choice).pack()
tk.Label(window, text="Computer's Choice:").pack()
tk.Label(window, textvariable=comp_choice).pack()
tk.Label(window, textvariable=result, font=("Arial", 14)).pack(pady=10)

# Buttons
for choice in choices:
    tk.Button(window, text=choice, command=lambda c=choice: play(c)).pack()

window.mainloop()
