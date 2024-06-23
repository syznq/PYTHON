import tkinter as tk
import random

def get_random_outcome():
    outcomes = ["You win!", "Try again!", "Better luck next time!"]
    return random.choice(outcomes)

def play_game():
    user_number = int(entry.get())
    outcome = get_random_outcome()
    result_label.config(text=outcome)

# Create the main window
root = tk.Tk()
root.title("Random Outcome Game")

# Create UI elements
label = tk.Label(root, text="Enter a number (1-10):")
entry = tk.Entry(root)
play_button = tk.Button(root, text="Play", command=play_game)
result_label = tk.Label(root, text="")

# Arrange UI elements
label.pack()
entry.pack()
play_button.pack()
result_label.pack()

# Start the GUI event loop
root.mainloop()
