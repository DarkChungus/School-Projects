import tkinter as tk
import matplotlib.pyplot as plt
import math
import numpy as np
import time
from sympy import *
from sympy.plotting import plot3d
from sympy.plotting import plot3d_parametric_surface
from sympy.plotting import plot3d_parametric_line
import sys
import random

def mandelbrot():
    import numpy as np
    import matplotlib.pyplot as plt

    def render(x_pixels, y_pixels, power_z, iteration_number, colormap):
        px = np.linspace(-2, 2, x_pixels)
        py = np.linspace(-2, 2, y_pixels)
        max_z = 2

        iterations = []

        for y in py:
            row = []
            for x in px:
                c = complex(x, y)
                z = 0
                for i in range(1, iteration_number):
                    if abs(z) >= max_z:
                        row.append(i)
                        break
                    else:
                        z = (z ** power_z) + c
                else:
                    row.append(0)

            iterations.append(row)

        axis = plt.axes()
        axis.set_aspect('equal')
        plt.colorbar(axis.pcolormesh(px, py, iterations, cmap=colormap))
        plt.xlabel("Real Axis")
        plt.ylabel("Imaginary Axis")
        plt.show()

    x_pixels = int(input("How many pixels for real axis? "))
    y_pixels = int(input("How many pixels for imaginary axis? "))
    power_z = int(input("What would be the power of z? "))
    iteration_number = int(input("How many iterations for the fractal? "))
    colormap = input("Please write a valid matplotlib colormap for the render: ")

    render(x_pixels, y_pixels, power_z, iteration_number, colormap)


def primes():
    import time

    def is_prime(num):
        x = 0
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                x += 1

        if x == 2:
            return True
        else:
            return False

    def search_pn(n):
        for k in range(2, n):
            x = 0
            for i in range(1, int(k / 2) + 1):
                if k % i == 0:
                    x += i

            if x == k:
                print(f'YES! {k} is a perfect number!')

    def search_mersenne(n):
        for i in range(1, n):
            if is_prime(i):
                possible = (2 ** i - 1)
                if is_prime(possible):
                    print(f'{i} is a Mersenne prime!')

    print("1. Perfect Number Searcher")
    time.sleep(.5)
    print("2. Mersenne Prime Searcher")
    time.sleep(.5)
    print()
    print()
    time.sleep(.5)
    choose = input("Type out which one you would like to use: ").lower()

    if choose[0] == 'p':
        n = int(input("Enter maximum limit for the Perfect Number Search: "))
        search_pn(n)
        done = True
    elif choose[0] == 'm':
        n = int(input("Enter maximum limit for the Mersenne Prime Search: "))
        search_mersenne(n)
        done = True
    else:
        print("Sorry! You have an invalid input.")
        time.sleep(1)
        print("Program reloading...")
        time.sleep(.5)
        primes()
        done = False

    if done:
        sys.exit()
    else:
        primes()


def calc():
    def main():
        x_coord = []
        y_coord = []
        x = symbols('x')

        print("---------------GRAPHING CALCULATOR------------------")
        print("---------------Choose your option:------------------")
        time.sleep(.5)
        print("1. Trigonometric Functions[hyperbolic, normal]")
        time.sleep(.5)
        print("2. Linear Function[ax + b]")
        time.sleep(.5)
        print("3. Quadratic Function[ax^2 + bx + c]")
        time.sleep(.5)
        print("4. Cubic Function[ax^3 + bx^2 + cx + d]")
        time.sleep(.5)
        print("5. Logarithmic Functions[log_a]")
        time.sleep(.5)
        print("6. 3D Plotter")
        print("------------------------------------------------------")
        time.sleep(.5)
        inp = input("Type out your choice: ").lower()
        if inp[0] == 't':
            print("__________________TRIGONOMETRY_______________________")
            print("|1. sinh(x)|2. cosh(x)|3. tanh(x)|")
            print("|4. sin(x) |5. cos(x) | 6. tan(x)|")
            print("----------------------------------------------------")
            print("----------------------------------")
            trig_pick = int(input("Pick any from 1-6: "))
            if trig_pick == 1:
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.sinh(n))
                    x_coord.append(i)

                plt.plot(x_coord, y_coord)
                plt.show()
            elif trig_pick == 2:
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.cosh(n))
                    x_coord.append(i)

                plt.plot(x_coord, y_coord)
                plt.show()
            elif trig_pick == 3:
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.tanh(n))
                    x_coord.append(i)

                plt.plot(x_coord, y_coord)
                plt.show()
            elif trig_pick == 4:

                plot(sin(x), (x, -7.5, 7.5), ylim=(-1.5, 1.5), xlabel="x", ylabel="y")

            elif trig_pick == 5:

                plot(cos(x), (x, -7.5, 7.5), ylim=(-1.5, 1.5), xlabel="x", ylabel="y")

            elif trig_pick == 6:

                plot(tan(x), (x, -10, 10), ylim=(-20, 20), xlabel="x", ylabel="y")

            else:
                print("Invalid Input! Please try again.")
                main()

        elif inp[0] == 'l':
            print("---------------LINEAR FUNCTION-------------------")
            print("-------------------ax + b------------------------")
            time.sleep(.5)
            linear_a = int(input("a: "))
            linear_b = int(input("b: "))
            print("-------------------------------------------------")
            plot((linear_a * x + linear_b), (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")
        elif inp[0] == 'q':
            print("--------------QUADRATIC FUNCTION-----------------")
            print("----------------ax^2 + bx + c--------------------")
            time.sleep(.5)
            quad_a = int(input("a: "))
            quad_b = int(input("b: "))
            quad_c = int(input("c: "))
            print("-------------------------------------------------")
            plot((quad_a * x ** 2 + quad_b * x + quad_c), (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")

        elif inp[0] == 'c':
            print("---------------------CUBIC FUNCTION--------------------")
            print("-----------------ax^3 + bx^2 + cx + d------------------")
            time.sleep(.5)
            cubic_a = int(input("a: "))
            cubic_b = int(input("b: "))
            cubic_c = int(input("c: "))
            cubic_d = int(input("d: "))
            print("-------------------------------------------------------")
            plot((cubic_a * x ** 3 + cubic_b * x ** 2 + cubic_c * x + cubic_d), (x, -10, 10), ylim=(-10, 10),
                 xlabel="x", ylabel="y")
        elif inp[1] == 'o':
            global log_eqn
            print("-----------------LOGARITHM FUNCTIONS--------------------")
            print("----------------------log_a(x)--------------------------")
            time.sleep(.5)
            print("1. Natural Logarithm (base-e)")
            time.sleep(.2)
            print("2. Logarithm (base x, x > 1)")
            time.sleep(.2)
            ln_log = input("Choose 1 or 2: ")
            if ln_log[0] == 'n':
                log_eqn = ln(x)
            elif ln_log[0] == 'l':
                base = int(input("Logarithm Base(a): "))
                log_eqn = log(x, base)
            else:
                print("Invalid Input! Please try again.")
                main()

            plot(log_eqn, (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")

        elif inp[0] == '3':
            print("---------------3 DIMENSIONAL PLOTTING------------------")
            time.sleep(.5)
            print("-------------------------------------------------------")
            print("1. z = x*y")
            print("2. z = x/y")
            print("3. z = cos(x), z = sin(x), z = x")
            print("4. z = cos(x + y), z = sin(x + y), z = x + y")
            print("5. z = x^2 + y^2")
            u, v = symbols("u v")

            input3d = int(input("Choose from 1-5: "))
            if input3d == 1:
                plot3d((u * v, (u, -5, 5), (v, -5, 5)))
            elif input3d == 2:
                plot3d((u / v, (u, -5, 5), (v, -5, 5)))
            elif input3d == 3:
                plot3d_parametric_line((cos(u), sin(u), u, (u, -5, 5)),
                                       (sin(u), u ** 2, u, (u, -5, 5)))
            elif input3d == 4:
                plot3d_parametric_surface(cos(u + v), sin(u - v), u - v,
                                          (u, -5, 5), (v, -5, 5))
            elif input3d == 5:
                plot3d((u ** 2 + v ** 2, (u, -5, 5), (v, -5, 5)))
            else:
                print("Invalid Input! Please try again.")
                main()
        else:
            print("Invalid Input! Please try again.")
            main()

    main()


def maclaurin():

    def e_power_x(x, n):
        taylor_approximation = 0
        for i in range(0, n):
            taylor_approximation += (x ** i) / math.factorial(i)

        return taylor_approximation

    def f_sin(x, n):
        taylor_approximation = 0
        for i in range(1, n):
            taylor_approximation += (-1) ** (i - 1) * (x ** (2 * i - 1) / math.factorial(2 * i - 1))
        return taylor_approximation

    def f_cos(x, n):
        taylor_approximation = 0
        for i in range(n):
            taylor_approximation += (-1) ** i * (x ** (2 * i) / math.factorial(2 * i))
        return taylor_approximation

    print("----------------------------------")
    print("| 1. sin(x) | 2. cos(x) | 3. e^x |")
    print("----------------------------------")
    time.sleep(.5)

    taylor_input = input("Choose a function to approximate: ")

    if taylor_input[0] == 's':

        iterations = int(input("How many iterations for the Taylor Series? "))

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05)
        sine = np.sin(x_range)

        figure, axes = plt.subplots()
        axes.plot(x_range, sine, color='black', linewidth=3)
        for i in range(1, iterations + 1):
            taylor_sine = [f_sin(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_sine)

        axes.set_ylim([-3, 3])
        legend = ['sin(x)']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of sin(x): {i} iterations')

        axes.legend(legend)
        plt.show()

    elif taylor_input[0] == 'c':

        iterations = int(input("How many iterations for the Taylor Series? "))

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05)
        cosine = np.cos(x_range)

        figure, axes = plt.subplots()
        axes.plot(x_range, cosine, color='black', linewidth=3)
        for i in range(1, iterations + 1):
            taylor_cosine = [f_cos(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_cosine)

        axes.set_ylim([-3, 3])

        legend = ['cos(x)']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of cos(x): {i} iterations')

        axes.legend(legend)
        plt.show()

    elif taylor_input[0] == 'e':

        iterations = int(input("How many iterations for the Taylor Series? "))

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05)
        e_x = np.exp(x_range)

        figure, axes = plt.subplots()
        axes.plot(x_range, e_x, color='black', linewidth=3)
        for i in range(1, iterations + 1):
            taylor_e = [e_power_x(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_e)

        axes.set_ylim([-3, 3])

        legend = ['e^x']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of e^x: {i} iterations')

        axes.legend(legend)
        plt.show()


def wpm():

    list = [
        'also', 'during', 'find', 'be', 'on', 'work', 'or', 'school', 'line', 'just', 'number',
        'any', 'become', 'many', 'do', 'as', 'both', 'down', 'hold', 'it', 'he', 'could', 'she',
        'become', 'who', 'present', 'any', 'when', 'into', 'no', 'and', 'how', 'help', 'leave',
        'know', 'face', 'will', 'way', 'govern', 'can', 'each', 'form', 'fact', 'system', 'ask',
        'very', 'of', 'make', 'work', 'program', 'eye', 'than', 'head', 'hand', 'would', 'give',
        'but', 'day'
    ]
    user_words = ""
    chosen_words = ""

    print("1. 10 Words")
    print("2. 30 Words")
    print("3. 50 Words")

    user_input = str(input("Enter which one you want to do: "))
    print()
    if user_input[0] == '1':
        for i in range(1, 11):
            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        user_words = str(input(""))
        end = time.time()
        length = end - start
        wpm = 600 / length

        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '2':
        for i in range(1, 31):
            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        user_words = str(input(""))
        end = time.time()
        length = end - start
        wpm = 1800 / length

        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '3':
        for i in range(1, 51):
            choice = random.choice(list)
            chosen_words = chosen_words + choice + " "

        print(chosen_words)
        print("Your input starts in...")
        time.sleep(.5)
        print(3)
        time.sleep(1)
        print(2)
        time.sleep(1)
        print(1)
        time.sleep(1)
        print("GO!")
        start = time.time()
        user_words = str(input(""))
        end = time.time()
        length = end - start
        wpm = 3000 / length

        print(f'You have {wpm} words per minute.')


def center_window(window):

    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


window = tk.Tk()

window.geometry("1000x1000")

label = tk.Label(window, text = "Some Cool Programs")
label.config(font=("Tahoma", 50))

label2 = tk.Label(window, text = "Made by Prakrit Gajurel")
label2.config(font=("Tahoma", 20))

label3 = tk.Label(window, text = "For IT Exhibition 2081")
label3.config(font=("Tahoma",20))

note = tk.Label(window, text = "Note: Please return to the console after pressing the button!")
note.config(font=("Tahoma",10), foreground="green")

button1 = tk.Button(window, command=mandelbrot, activebackground="red", activeforeground="white", cursor="hand2", text="Mandelbrot Render")
button2 = tk.Button(window, command=primes, activebackground="orange", activeforeground="white", cursor="hand2", text="Prime Programs")
button3 = tk.Button(window, command=calc, activebackground="green", activeforeground="white", cursor="hand2", text="Graph your equations!")
button4 = tk.Button(window, command=maclaurin, activebackground="blue", activeforeground="white", cursor="hand2", text="Approximate Function!")
button5 = tk.Button(window, command=wpm, activebackground="purple", activeforeground="white", cursor="hand2", text="See how fast you can type!")

label.pack()
label2.pack()
label3.pack()
button1.pack(pady=30)
button2.pack(pady=30)
button3.pack(pady=30)
button4.pack(pady=30)
button5.pack(pady=30)
note.pack()

center_window(window)
window.mainloop()
