import tkinter as tk

def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying and entering text
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create and place buttons in the grid
row_val = 1
col_val = 0
for button_text in buttons:
    tk.Button(root, text=button_text, padx=20, pady=20, font=('Arial', 16), command=lambda text=button_text: on_click(text)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear and equal buttons
tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row_val, column=0)
tk.Button(root, text="=", padx=20, pady=20, font=('Arial', 16), command=calculate).grid(row=row_val, column=1, columnspan=3)

# Run the application
root.mainloop()
