# Import module
from tkinter import *
from PIL import ImageTk, Image

# Create object
root = Tk()

# Adjust size
root.geometry("400x400")

# Add image file
bg = ImageTk.PhotoImage(file = "/home/roia/stuff/1652109861_16-titis-org-p-beautiful-black-women-in-the-nude-krasivay-20.jpg")
water = ImageTk.PhotoImage(file = "images/origami_logo_window.png")
# Create Canvas
canvas1 = Canvas( root, width = 400,
				height = 400)

canvas1.pack(fill = "both", expand = True)



# Display image





# Add Text
canvas1.create_text( 200, 250, text = "Welcome")

# Create Buttons
button1 = Button( root, text = "Exit")
button3 = Button( root, text = "Start")
button2 = Button( root, text = "Reset")




# Display Buttons
button1_canvas = canvas1.create_window( 100, 10,
									anchor = "nw",
									window = button1)

button2_canvas = canvas1.create_window( 100, 40,
									anchor = "nw",
									window = button2)

button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",
									window = button3)

# drag callbacks
dragged_item = None
current_coords = 0, 0

def start_drag(event):
    global current_coords
    global dragged_item
    result = canvas1.find_withtag('current')
    if result:
        dragged_item = result[0]
        current_coords = canvas1.canvasx(event.x), canvas1.canvasy(event.y)
    else:
        dragged_item = None

def stop_drag(event):
    dragged_item = None
    print(current_coords)

def drag(event):
    global current_coords
    xc, yc = canvas1.canvasx(event.x), canvas1.canvasy(event.y)
    dx, dy = xc - current_coords[0], yc - current_coords[1]
    current_coords = xc, yc
    canvas1.move(dragged_item, dx, dy)


# bind 'draggable' tag to mouse events
canvas1.tag_bind('draggable', '<ButtonPress-1>', start_drag)
canvas1.tag_bind('draggable', '<ButtonRelease-1>', stop_drag)
canvas1.tag_bind('draggable', '<B1-Motion>', drag)

canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.create_image(0, 0, image = water, anchor="nw", tag = "draggable")

# def make_draggable(widget):
#     widget.tag_bind("dragged", "<Button-1>", on_drag_start)
#     widget.tag_bind("dragged",  "<B1-Motion>", on_drag_motion)

# def on_drag_start(event):
#     widget = event.widget
#     widget._drag_start_x = event.x
#     widget._drag_start_y = event.y

# def on_drag_motion(event):
#     widget = event.widget
#     x = widget.winfo_x() - widget._drag_start_x + event.x
#     y = widget.winfo_y() - widget._drag_start_y + event.y
#     widget.place(x=x, y=y)

# make_draggable(canvas1)   

# Execute tkinter
root.mainloop()
