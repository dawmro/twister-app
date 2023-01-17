import tkinter as tk


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

# run app
root.mainloop()