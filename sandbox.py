from tkinter import *
from PIL import ImageTk, Image, ImageDraw, ImageFont
from tkinter import filedialog as fd
import math


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

def choose_image():
    global chosen_img, image_height, image_width
    file_name = image_file_name("Choose An Image")
    chosen_img = Image.open(file_name)
    image_size = chosen_img.size

    # resize image to fit the window maintaining ratio
    image_width = image_size[0]
    image_height = image_size[1]

    if image_width > 520:
        new_image_width = image_width - (image_width - 520)
        new_image_height = math.floor(image_height / (image_width / new_image_width))
    elif image_height > 600:
        new_image_height = image_height - (image_height - 600)
        new_image_width = math.floor(image_width / (image_height / new_image_height))
    else:
        new_image_width = image_width
        new_image_height = image_height

    # center the picture in the canvas
    left_space = 600 - new_image_height
    new_y_position = math.floor(left_space/2)


    chosen_img = chosen_img.resize((new_image_width, new_image_height), Image.ANTIALIAS)
    new_chosen_img = ImageTk.PhotoImage(chosen_img)
    right_canvas.create_image(0, 0, image=new_chosen_img, anchor="nw")
    right_canvas.place(x=290, y=new_y_position)
    right_canvas.image = new_chosen_img




def choose_watermark():

    file_name = image_file_name("Choose A Watermark")
    gfg = GFG(file_name, root)
	# This will bind arrow keys to the tkinter
	# toplevel which will navigate the image or drawing
    root.bind("<KeyPress-Left>", lambda e: gfg.left(e))
    root.bind("<KeyPress-Right>", lambda e: gfg.right(e))
    root.bind("<KeyPress-Up>", lambda e: gfg.up(e))
    root.bind("<KeyPress-Down>", lambda e: gfg.down(e))



def close_add_text_win(top):
   text_to_watermark = inserted_text.get()
   top.destroy()
   draw =ImageDraw.Draw(chosen_img)
   font = ImageFont.truetype("yaci.ttf", 35)
   text_width, text_height =  draw.textsize(text_to_watermark, font)

   # calculate the x,y coordinates of the text
   margin = 10
   x = image_width - text_width - margin
   y = image_height - text_height - margin
   values = {
    "image width": image_width,
    "image height": image_height,
    "text width" : text_width,
    "text height" : text_height,
    "x" : x,
    "y" : y
   }
   print(f"\n {values} \n")

    # draw watermark in the bottom right corner
   draw.text((x, y), text_to_watermark, font=font)
#    chosen_img.show()

    #Save watermarked image
   chosen_img.save('images/watermark.jpg')


def popupwin():
   global inserted_text
   #Create a Toplevel window
   top= Toplevel(root)
   top.geometry("450x200")
   top.title("Add text to watermark")
   inserted_text = StringVar()

   #list of fonts
   fonts = [
	"Lato",
	"Noto Sans",
	"Helvetica",
	"Times Roman"
    ]

    # datatype of menu text
   clicked = StringVar()

    # initial menu text
   clicked.set( "Choose A Font" )

   #Create an Entry Widget in the Toplevel window
   entry= Entry(top, textvariable=inserted_text,width= 25)
   entry.place(x=100, y=50)
   # Create Dropdown menu
   drop = OptionMenu( top , clicked , *fonts )
   drop.place(x=130, y=80)

   #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Insert Text",command=lambda:close_add_text_win(top))
   button.place(x=150, y=120)


# root window
root = Tk()
root.title("Origami Image WatermarK")
root.geometry("800x600")

#-------------------------Left side of the screen---------------------------------#
# logo
canvas = Canvas(width=221, height=332)
logo_img = PhotoImage(file="images/origami_logo_window.png")
canvas.create_image(115, 135, image=logo_img)
canvas.place(x=10, y=2)

# Buttons
choose_image_button = Button(text="Choose Image", command=choose_image)
choose_watermark_button = Button(text="Choose Watermark Image", command=choose_watermark)
text_watermark = Button(text="Add Text Watermark", command=popupwin)

# Labels
choose_image_label = Label(text="Select a picture to add watermark to it")
watermark_type = Label(text="Add a picture or a text Watermark")

# widget placement on screen
choose_image_label.place(x=5, y=260)
choose_image_button.place(x=60, y=290)
watermark_type.place(x=8, y=380)
choose_watermark_button.place(x=20, y=410)
text_watermark.place(x=38, y=460)

#------------------------- Line on screen ---------------------------------#
line_canvas = Canvas(width=10, height=1200)
line_canvas.place(x=280, y=0)
line_canvas.create_line(2, 0, 2, 1200)

#-------------------------Right side of the screen---------------------------------#
right_canvas = Canvas(width=520, height=600)
right_canvas.place(x=290, y=0)



# root.bind('<Configure>', resizer)

root.mainloop()
