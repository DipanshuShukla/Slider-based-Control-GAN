from tkinter import *

master = Tk()
for i in range(50):
	w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
	w.pack()

mainloop()