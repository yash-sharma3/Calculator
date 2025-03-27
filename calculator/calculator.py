import tkinter as tk
from tkinter import messagebox

def on_click(event):
    text = event.widget.cget("text")
    process_input(text)

def process_input(text):
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry_var.set("")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + str(text))

def on_key(event):
    key = event.char
    if key.isdigit() or key in "+-*/":
        process_input(key)
    elif event.keysym == "Return":
        process_input("=")
    elif event.keysym == "BackSpace":
        entry_var.set(entry_var.get()[:-1])
    elif event.keysym == "Escape":
        entry_var.set("")

root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.configure(bg="#2C3E50")
root.bind("<Key>", on_key)

entry_var = tk.StringVar()

top_frame = tk.Frame(root, bg="#2C3E50")
top_frame.pack()

entry = tk.Entry(top_frame, textvar=entry_var, font="Arial 24 bold", justify="right", bd=10, relief=tk.GROOVE, bg="#ECF0F1", fg="#2C3E50")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    frame = tk.Frame(button_frame, bg="#2C3E50")
    frame.pack()
    for btn in row:
        button = tk.Button(frame, text=btn, font="Arial 18 bold", width=5, height=2, bg="#34495E", fg="#ECF0F1", bd=3, relief=tk.RAISED)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", on_click)

root.mainloop()
