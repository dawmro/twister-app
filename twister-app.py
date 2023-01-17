import tkinter as tk
from PIL import ImageTk


BG_COLOUR = "#ffffff"


# function to load frame1
def load_frame1():
    
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
    print("Wheel is spinning!")


# initiallize app
root = tk.Tk()

# add app title
root.title("Twister App")

# center app on the screen
root.eval("tk::PlaceWindow . center")

# create first frame
frame1 = tk.Frame(root, width=506, height=630, bg=BG_COLOUR)

# place frame on the page
frame1.grid(row=0, column=0)




    
    


# run app
root.mainloop()