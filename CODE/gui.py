from tkinter import *
from tkinter import messagebox   
  
top = Tk()  
  
#THE MAIN WINDOW

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

# NO RESIZE
top.resizable(False, False)

#ICON
top.iconbitmap("./assets/dc.ico")




#BUTTONS 
def Content_Rating():  
    messagebox.showinfo("Deon", "Content Ratings clicked")  

def Trend():  
    messagebox.showinfo("Deon", "Trend button clicked")  

def Top_Directors():  
    messagebox.showinfo("Deon", "Top 5 Directors clicked")  

def Top_Actors():  
    messagebox.showinfo("Deon", "Top 5 Actors clicked")  

def Sentiment():  
    messagebox.showinfo("Deon", "Sentiment Analysis Clicked")    

  
b1 = Button(top,text = "Content Ratings",command = Content_Rating,activeforeground = "red",activebackground = "pink",pady=10, height=1, width=15)  
  
b2 = Button(top, text = "Trend",command=Trend, activeforeground = "blue",activebackground = "pink",pady=10, height=1, width=15)  
  
b3 = Button(top, text = "Top Directors", command=Top_Directors, activeforeground = "green",activebackground = "pink",pady = 10, height=1, width=15)  
  
b4 = Button(top, text = "Top 5 Actors", command=Top_Actors, activeforeground = "yellow",activebackground = "pink",pady = 10, height=1, width=15)  

b5 = Button(top, text = "Sentiment Analysis", command=Sentiment, activeforeground = "yellow",activebackground = "pink",pady = 10, height=1, width=15)
  
b1.pack()   
b2.pack()  
b3.pack()  
b4.pack()  
b5.pack()
  
top.mainloop()  