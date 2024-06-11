import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.title("Miles to Kilometers Converter")
window.geometry("500x250")

title_label = ttk.Label(
    window, text="Miles to Kilometers Converter", font="Times 20 bold"
)
title_label.pack()


window.mainloop()
