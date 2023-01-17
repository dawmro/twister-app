import tkinter as tk
from PIL import ImageTk

# initiallize app
root = tk.Tk()

# add app title
root.title("Twister App")

# center app on the screen
root.eval("tk::PlaceWindow . center")

# create first frame
frame1 = tk.Frame(root, width=400, height=400, bg="#ffffff")

# place frame on the page
frame1.grid(row=0, column=0)

# load image for main screen
main_screen_img = ImageTk.PhotoImage(file="assets/main_screen.png")

# convert image to widget for frame1
main_screen_widget = tk.Label(frame1, image=main_screen_img)
main_screen_widget.image = main_screen_img

# pack widget to place it in frame
main_screen_widget.pack()

# run app
root.mainloop()