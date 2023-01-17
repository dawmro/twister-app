import tkinter as tk
from PIL import ImageTk
import random
from random import randrange


BG_COLOUR = "#ffffff"


# function to load frame1
def load_frame1():
    # raise frame1 on top
    frame1.tkraise()
    
    # prevent child form modifying parent
    frame1.pack_propagate(False)
    
    # load image for main screen
    main_screen_img = ImageTk.PhotoImage(file="assets/main_screen.png")

    # convert image to widget for frame1
    main_screen_widget = tk.Label(frame1, image=main_screen_img, bg=BG_COLOUR)
    main_screen_widget.image = main_screen_img

    # pack widget to place it in frame
    main_screen_widget.pack()

    # create widget with text for frame1
    tk.Label(
        frame1,
        text="take it for a spin",
        bg=BG_COLOUR,
        fg="black",
        font=("TkHeadingFont", 24)
    ).pack()

    # create button widget
    tk.Button(
        frame1,
        text="SPIN THE WHEEL",
        font=("TkDefaultFont", 24),
        bg="#888888",
        fg="white",
        cursor="hand2",
        activebackground="#123456",
        activeforeground="red",
        command=lambda:load_frame2()
    ).pack(pady=20)


# function to load frame2
def load_frame2():
    # raise frame2 on top
    frame2.tkraise()
    print(get_random_position())
    
    
def get_random_position():
    positions = {
        1 : "right hand green",
        2 : "right hand red",
        3 : "right hand yellow",
        4 : "right hand blue",
        5 : "right foot green",
        6 : "right foot red",
        7 : "right foot yellow",
        8 : "right foot blue",
        9 : "left hand green",
        10 : "left hand red",
        11 : "left hand yellow",
        12 : "left hand blue",
        13 : "left foot green",
        14 : "left foot red",
        15 : "left foot yellow",
        16 : "left hand blue",
    }
    return positions[randrange(1, len(positions), 1)]


# initiallize app
root = tk.Tk()

# add app title
root.title("Twister App")

# center app on the screen
root.eval("tk::PlaceWindow . center")

# create first frame
frame1 = tk.Frame(root, width=506, height=630, bg=BG_COLOUR)

# create second frame
frame2 = tk.Frame(root, bg=BG_COLOUR)

# place first frame on the page
#frame1.grid(row=0, column=0)

# place second frame on the page
#frame2.grid(row=0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)


load_frame1()

    
    


# run app
root.mainloop()