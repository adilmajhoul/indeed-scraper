import tkinter as tk


def on_button_click():
    print("Button clicked!")


root = tk.Tk()
root.title("Button Example")

# Create a button widget
button = tk.Button(root, text="Click Me", command=on_button_click)

root.mainloop()
