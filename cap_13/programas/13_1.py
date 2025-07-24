import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("primeira janela")
root.geometry("1920x1080")

frame = ttk.Frame(root)
text = ttk.Label(frame, text="Ola GUI!")
text.pack()

button = ttk.Button(frame, text="Sai", command=root.destroy)
button.pack()

frame.pack(expand=True)

root.mainloop()
