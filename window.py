from tkinter import *
from functions import *
from PIL import ImageTk

# color scheme
SECONDARY_COLOR = "#2B2B2B"
PRIMARY_COLOR = "#242424"
BACKGROUND_BUTTON = "#1F6AA5"
   

# root window
root = Tk()
root.title("Origami Image Watermark")
root.geometry("1100x580")

#-------------------------Right side of the screen---------------------------------#
right_canvas = Canvas(root, width=810, height=580)
right_canvas.place(x=290, y=0)

#-------------------------Left side of the screen---------------------------------#
# logo
canvas = Canvas(width=221, height=332)
logo_img = PhotoImage(file="images/origami_logo_window.png")
canvas.create_image(115, 135, image=logo_img)
canvas.place(x=10, y=2)


# widgets
choose_image_label = Label(text="Select a picture to add watermark to it")
choose_image_label.place(x=5, y=260)

choose_image_button = Button(text="Choose Image", command=lambda: choose_image(right_canvas))
choose_image_button.place(x=60, y=290)

watermark_type = Label(text="Add a picture or a text Watermark")
watermark_type.place(x=8, y=380)

choose_watermark_button = Button(text="Choose Watermark Image", command=lambda: choose_watermark(right_canvas, root))
choose_watermark_button.place(x=20, y=410)

text_watermark = Button(text="Add Text Watermark", command=lambda: popupwin(root, right_canvas))
text_watermark.place(x=38, y=460)

save_image_button = Button(text="Save Image", command=lambda: save_image(root))
save_image_button.place(x=68, y=500)

root.mainloop()