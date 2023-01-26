import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

button = tk.Button()
button_load = Image.open('images/origami_logo_window.png')
root.button_img = ImageTk.PhotoImage(button_load)
button.config(image=root.button_img)

button.pack(side='top')

root.mainloop()