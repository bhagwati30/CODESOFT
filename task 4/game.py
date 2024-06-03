import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result_text = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"
    
    if user_choice == computer_choice:
        result_text += "It's a tie!"
        result_label.config(text=result_text)
        return
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        result_text += "You win!"
        global user_score
        user_score += 1
    else:
        result_text += "You lose!"
        global computer_score
        computer_score += 1

    result_label.config(text=result_text)
    score_label.config(text=f"Score - You: {user_score} Computer: {computer_score}")

# Function to reset the game
def play_again():
    result_label.config(text="")
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        result_label.config(text="")
    else:
        root.quit()

# Main GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("500x300")  # Set the size of the window

# Initialize scores
user_score = 0
computer_score = 0

# GUI Components
instructions_label = tk.Label(root, text="Choose rock, paper, or scissors:", font=("Helvetica", 16))
instructions_label.pack(pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack(pady=20)

rock_button = tk.Button(buttons_frame, text="Rock", command=lambda: determine_winner('rock'), height=2, width=10)
rock_button.grid(row=0, column=0, padx=20, pady=10)

paper_button = tk.Button(buttons_frame, text="Paper", command=lambda: determine_winner('paper'), height=2, width=10)
paper_button.grid(row=0, column=1, padx=20, pady=10)

scissors_button = tk.Button(buttons_frame, text="Scissors", command=lambda: determine_winner('scissors'), height=2, width=10)
scissors_button.grid(row=0, column=2, padx=20, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Score - You: {user_score} Computer: {computer_score}", font=("Helvetica", 14))
score_label.pack(pady=10)

play_again_button = tk.Button(root, text="Play Again", command=play_again, font=("Helvetica", 14), height=2, width=15)
play_again_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
