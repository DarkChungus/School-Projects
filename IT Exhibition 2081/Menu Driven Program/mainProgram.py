# Import all the required functions and librariess

import tkinter as tk
from fractalRender import mandelbrot
from numberTheory import nt_problems
from graphingCalculator import calc
from taylorSeries import maclaurin
from typingTest import wpm
from centerWindow import center_window


window = tk.Tk() # Creating the TKinter window

window.geometry("1000x1000") # The width and height of the window

# Making and configuring all the texts

label = tk.Label(window, text = "Some Cool Programs")
label.config(font=("Tahoma", 50))

label2 = tk.Label(window, text = "Made by Prakrit Gajurel")
label2.config(font=("Tahoma", 20))

label3 = tk.Label(window, text = "For IT Exhibition 2081")
label3.config(font=("Tahoma",20))

note = tk.Label(window, text = "Note: Please return to the console after pressing the button!")
note.config(font=("Tahoma",10), foreground="green")

# Creating all the buttons

button1 = tk.Button(window, command=mandelbrot, activebackground="red", activeforeground="white", cursor="hand2", text="Mandelbrot Render")
button2 = tk.Button(window, command=nt_problems, activebackground="orange", activeforeground="white", cursor="hand2", text="Number Theory Programs")
button3 = tk.Button(window, command=calc, activebackground="green", activeforeground="white", cursor="hand2", text="Graph your equations!")
button4 = tk.Button(window, command=maclaurin, activebackground="blue", activeforeground="white", cursor="hand2", text="Approximate Function!")
button5 = tk.Button(window, command=wpm, activebackground="purple", activeforeground="white", cursor="hand2", text="See how fast you can type!")

# Packing all the widgets

label.pack()
label2.pack()
label3.pack()
button1.pack(pady=30)
button2.pack(pady=30)
button3.pack(pady=30)
button4.pack(pady=30)
button5.pack(pady=30)
note.pack()
window.title("IT Exhibition 2081") # Changing the title of the window

center_window(window) # Centering the window using the function
window.mainloop() # Making the window run
