import tkinter as tk 
import requests

HEIGHT = 500
WIDTH = 600

def testfunction():
	print("Button clicked")

root = tk.Tk()

#root.title("Networktest")
#root.geometry("480x480")
background_image = tk.PhotoImage(file='net.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

canvas = tk.Canvas(root, height = HEIGHT, width =WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = '#80c1ff', bd = 5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font = 40)
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text='Run', bg='gray' , font = 40,command=testfunction())
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gray', bd = 10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
