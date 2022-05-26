from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Data Analysis")
# open image file
bg = ImageTk.PhotoImage(file="si.png")
# create canvas
canvas = Canvas(root, width=500, height=500)
canvas.pack(fill=BOTH, expand=True)
# place the image inside canvas
canvas.create_image(0, 0, image=bg, anchor='nw')
# resize function for resizing the image
# with proper width and height of root window
def resize_bg(event):
    global bgg, resized, bg2
    # open image to resize it
    bgg = Image.open("si.png")
    # resize the image with width and height of root
    resized = bgg.resize((event.width, event.height),
                         Image.ANTIALIAS)
    
    bg2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=bg2, anchor='nw')
# bind resized function with root window
root.bind("<Configure>", resize_bg)
root.mainloop()




