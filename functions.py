from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import math
import matplotlib.pyplot as plt

# drag callbacks
dragged_item = None
current_coords = 0, 0
image_watermark_present = 0
text_watermark_present = 0

def start_drag(event):
    global current_coords
    global dragged_item
    result = moveable_canvas.find_withtag('current')
    if result:
        dragged_item = result[0]
        current_coords = moveable_canvas.canvasx(event.x), moveable_canvas.canvasy(event.y)
    else:
        dragged_item = None

def stop_drag(event):
    dragged_item = None
    

def drag(event):
    global current_coords
    xc, yc = moveable_canvas.canvasx(event.x), moveable_canvas.canvasy(event.y)
    dx, dy = xc - current_coords[0], yc - current_coords[1]
    current_coords = xc, yc
    moveable_canvas.move(dragged_item, dx, dy)

def make_draggable(moveable_canvas):
    # bind 'draggable' tag to mouse events
    moveable_canvas.tag_bind('draggable', '<ButtonPress-1>', start_drag)
    moveable_canvas.tag_bind('draggable', '<ButtonRelease-1>', stop_drag)
    moveable_canvas.tag_bind('draggable', '<B1-Motion>', drag)



def image_file_name(prompt_title):
    filetypes = (
        ('jpg files', '*.jpg'),
        ('png files', '*.png'),
        ('jpeg files', '*.jpeg')
    )

    file_name = fd.askopenfilename(
        title=prompt_title,
        initialdir='/home/roia/stuff',
        filetypes=filetypes)

    return file_name

def choose_image(right_canvas):

    global mid_height, mid_width, bg, chosen_img, image_height, image_width
    file_name = image_file_name("Choose Image")
    chosen_img = Image.open(file_name)
    image_size = chosen_img.size

    # resize image to fit the window maintaining ratio
    image_width = image_size[0]
    image_height = image_size[1]

    if image_width > 810:
        new_image_width = image_width - (image_width - 810)
        new_image_height = math.floor(image_height / (image_width / new_image_width))
    elif image_height > 580:
        new_image_height = image_height - (image_height - 580)
        new_image_width = math.floor(image_width / (image_height / new_image_height))
    else:
        new_image_width = image_width
        new_image_height = image_height

    # center the picture in the canvas
    left_y_space = 580 - new_image_height
    new_y_position = math.floor(left_y_space/2)
    left_x_space = 810 - new_image_width
    new_x_position = (math.floor(left_x_space/2))

    # global variables to be used to place watermark
    mid_height = new_y_position + math.floor(new_image_height / 2)
    mid_width = new_x_position + math.floor(new_image_width / 2)

    chosen_img = chosen_img.resize((new_image_width, new_image_height), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(chosen_img)
    place_image(right_canvas, new_x_position, new_y_position)
        

def choose_watermark(right_canvas, root):

    try:
        global moveable_canvas, watermark_image, new_image_height_wm, new_image_width_wm, watermark_img
        moveable_canvas = right_canvas
        file_name = image_file_name("Choose Image")
        watermark_img = Image.open(file_name)
        image_width = watermark_img.size[0]
        image_height = watermark_img.size[1]

        # resize watermark images
        if image_width > 200:
            new_image_width_wm = image_width - (image_width - 200)
            new_image_height_wm = math.floor(image_height / (image_width / new_image_width_wm))
        elif image_height > 300:
            new_image_height_wm = image_height - (image_height - 300)
            new_image_width_wm = math.floor(image_width / (image_height / new_image_height_wm))
        else:
            new_image_width_wm = image_width
            new_image_height_wm = image_height

        watermark_img = watermark_img.resize((new_image_width_wm, new_image_height_wm), Image.ANTIALIAS)
        watermark_image = ImageTk.PhotoImage(watermark_img)
        place_watermark_image(right_canvas, mid_width, mid_height)
    except NameError:
        error_popup(root, "You need to choose and image first")

def place_image(right_canvas, xcor=0, ycor=0):
    right_canvas.create_image( xcor, ycor, image = bg, anchor = "nw")

def place_watermark_image(right_canvas, xcor=0, ycor=0):
    global image_watermark_present
    image_watermark_present = 1
    right_canvas.create_image( xcor, ycor, image = watermark_image, tag = "draggable", anchor = "nw")
    make_draggable(moveable_canvas)


def close_add_text_win(top):
   full_font_arg = ""
   text_to_watermark = inserted_text.get()
   watermark_color = color.get()
   font = clicked.get()
   font_size = clicked_size.get()
   if font != "":
    full_font_arg = font
   else:
    full_font_arg = "Arial"

   if font_size != "":
    full_font_arg = f"{full_font_arg} {font_size} bold"
   else:
    full_font_arg = f"{full_font_arg} 20 bold"

   font_tuple = (full_font_arg)
   top.destroy()
   place_text(moveable_canvas, text_to_watermark, font_tuple, watermark_color)


def popupwin(root, right_canvas):
   global inserted_text, moveable_canvas, color, clicked, clicked_size, error_root
   moveable_canvas = right_canvas
   error_root = root
   #Create a Toplevel window
   top= Toplevel(root)
   top.geometry("450x250")
   top.title("Add text to watermark")
   inserted_text = StringVar()
   color = StringVar()

   
   fonts = [
    "Arial",
	"Helvetica",
    "Lato"
    ]
    
   font_size = [
        5,
        10,
        15,
        20,
        25,
        30,
        35,
        40,
        45,
        50
    ]

    # datatype of menu text
   clicked = StringVar()
   clicked_size = StringVar()

    # initial menu text
   clicked.set( "Choose A Font" )
   clicked_size.set("Choose Font Size")

   # top level widgets
   insert_text_label = Label(top, text="Insert Text for Watermark")
   insert_text_label.pack(pady=10)

   entry= Entry(top, textvariable=inserted_text,width= 25)
   entry.pack()

   drop = OptionMenu( top , clicked , *fonts )
   drop.pack()

   drop_size = OptionMenu( top , clicked_size , *font_size )
   drop_size.pack()

   color_text_label = Label(top, text="Insert Color for Watermark")
   color_text_label.pack(pady=10)

   entry= Entry(top, textvariable=color,width= 25)
   entry.pack()
   
   button= Button(top, text="Insert Text",command=lambda:close_add_text_win(top))
   button.pack()


def place_text(right_canvas, inserted_text, font_tuple, color="white"):
   try:
    global text_watermark_present
    text_watermark_present = 1
    right_canvas.create_text(mid_width, mid_height, text=inserted_text, fill= color, font = font_tuple, tags= "draggable")
    make_draggable(moveable_canvas)
   except NameError:
    error_popup(error_root, "You need to pick an image first")

def close_error_popup(error):
    error.destroy()

def error_popup(root, error_message):
   #Create a Toplevel window
   error= Toplevel(root)
   error.geometry("300x100")
   error.title("Oops there is a problem")
 
   # top level widgets
   error_text_label = Label(error, text=error_message)
   error_text_label.pack(pady=20)
   
   error_button= Button(error, text="Okay",command=lambda:close_error_popup(error))
   error_button.pack()

def save_image(root):
    watermark_size = (new_image_width_wm, new_image_height_wm)
    watermark_img.thumbnail(watermark_size)
    size_on_watermark = (math.floor(current_coords[0] - new_image_width_wm), math.floor(current_coords[1] - new_image_height_wm), new_image_width_wm, new_image_height_wm)
    print(size_on_watermark)
    print(f"{image_width}x{image_height}")
    chosen_img.paste(watermark_img, size_on_watermark)
    print("we have done that")
    chosen_img.save("watermark_image.jpg")
            # files = [('All Files', '*.*'), 
            #  ('Python Files', '*.py'),
            #  ('Text Document', '*.txt')]
            # file = fd.asksaveasfile(filetypes = files, defaultextension = files)
