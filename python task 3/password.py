import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, complexity):
    characters = string.ascii_letters  # Default to letters only
    if complexity == 1:  # Letters and digits
        characters += string.digits
    elif complexity == 2:  # Letters, digits, and special characters
        characters += string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    def generate():
        try:
            length = int(entry_length.get())
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a positive integer for the password length.")
            return

        complexity = complexity_var.get()
        password = generate_password(length, complexity)
        label_result.config(text=f"Generated Password: {password}")

    # Set up the main window
    root = tk.Tk()
    root.title("Password Generator")

    # Password Length
    tk.Label(root, text="Enter Password Length:").pack(pady=5)
    entry_length = tk.Entry(root)
    entry_length.pack(pady=5)

    # Password Complexity
    tk.Label(root, text="Select Password Complexity:").pack(pady=5)
    complexity_var = tk.IntVar(value=0)
    tk.Radiobutton(root, text="Letters Only", variable=complexity_var, value=0).pack(anchor=tk.W)
    tk.Radiobutton(root, text="Letters and Digits", variable=complexity_var, value=1).pack(anchor=tk.W)
    tk.Radiobutton(root, text="Letters, Digits, and Special Characters", variable=complexity_var, value=2).pack(anchor=tk.W)

    # Generate Button
    tk.Button(root, text="Generate Password", command=generate).pack(pady=10)

    # Result Label
    label_result = tk.Label(root, text="Generated Password: ")
    label_result.pack(pady=5)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
