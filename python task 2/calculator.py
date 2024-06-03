import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_choice.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        else:
            result = "Invalid Operation"

        result_label.config(text=f"Result: {result}")
    except ValueError:
        result_label.config(text="Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create and place the first number entry
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# Create and place the second number entry
tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create and place the operation dropdown
tk.Label(root, text="Choose operation:").grid(row=2, column=0, padx=10, pady=10)
operation_choice = ttk.Combobox(root, values=['+', '-', '*', '/'])
operation_choice.grid(row=2, column=1, padx=10, pady=10)
operation_choice.current(0)  # Set default operation to +

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
