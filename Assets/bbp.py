from tkinter import *
top= Tk()

top.title("Deon Chris")
window_width = 500
window_height = 300

# get the screen dimension
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
top.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')