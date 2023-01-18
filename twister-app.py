import tkinter as tk
from PIL import ImageTk
import random
from random import randrange
import pathlib


BG_COLOUR = "#ffffff"

# results images location
RESULTS_IMAGES_DIR = 'assets/spin_results'

# load all result image files
RESULTS_FILES = [item for item in pathlib.Path(RESULTS_IMAGES_DIR).rglob('*.png') if item.is_file()]


# remove all widgets form screen
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# function to load frame1
def load_frame1():
    
    # raise frame1 on top
    frame1.tkraise()
    
    # prevent child form modifying parent
    frame1.pack_propagate(False)
    
    # load image for main screen
    main_screen_img = ImageTk.PhotoImage(file="assets/main_screen/main_screen.png")

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
    # clear app screen
    clear_widgets(frame1)
    clear_widgets(frame2)
    
    # raise frame2 on top
    frame2.tkraise()
    
    # load image for current screen
    random_img = ImageTk.PhotoImage(file=random.choice(RESULTS_FILES))

    # convert image to widget for frame2
    random_img_widget = tk.Label(frame2, image=random_img, bg=BG_COLOUR)
    random_img_widget.image = random_img

    # pack widget to place it in frame
    random_img_widget.pack()
    
    # create widget with text for frame1
    tk.Label(
        frame2,
        text="take it for a spin",
        bg=BG_COLOUR,
        fg="black",
        font=("TkHeadingFont", 24)
    ).pack()
    
    # create button widget
    tk.Button(
        frame2,
        text="SPIN THE WHEEL",
        font=("TkDefaultFont", 24),
        bg="#888888",
        fg="white",
        cursor="hand2",
        activebackground="#123456",
        activeforeground="red",
        command=lambda:load_frame2()
    ).pack(pady=20)   


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

# place frames on grid
for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

# load first frame
load_frame1()
    
# run app
root.mainloop()