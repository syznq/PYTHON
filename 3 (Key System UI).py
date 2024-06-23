import tkinter as tk

def check_key(user_key):
    predefined_key = "TestingKeySystem"
    return user_key == predefined_key

def validate_key():
    user_key = entry.get()
    if check_key(user_key):
        result_label.config(text="Access granted! Welcome.")
    else:
        result_label.config(text="Invalid key. Access denied.")

# Create the main window
root = tk.Tk()
root.title("Key Validation")

# Create UI elements
label = tk.Label(root, text="Enter the key:")
entry = tk.Entry(root)
validate_button = tk.Button(root, text="Validate", command=validate_key)
result_label = tk.Label(root, text="")

# Arrange UI elements
label.pack()
entry.pack()
validate_button.pack()
result_label.pack()

# Start the GUI event loop
root.mainloop()
