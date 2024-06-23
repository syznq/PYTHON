import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    charset = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(charset) for _ in range(length))
    password_label.config(text=f"Generated Password: {password}")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Add widgets
length_label = tk.Label(root, text="Password Length:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate", command=generate_password)
password_label = tk.Label(root, text="")

# Grid layout
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
password_label.grid(row=2, columnspan=2, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
