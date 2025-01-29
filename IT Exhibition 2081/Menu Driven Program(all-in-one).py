# Importing all the required libraries

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
    """
    A mandelbrot set is a fractal that is created by iterating this function:
    ===============
    z_n+1 = (z_n)^2 + c,
    ===============
    where c is any complex number. If you iterate it, and it starts to diverge, then you can assign a color
    to the mandelbrot set based on how quickly it diverges. If it does not diverge, and rather starts to
    converge, then you can color it fully black. This creates very interesting patterns.
    :return:
    """
    def render(x_pixels, y_pixels, power_z, iteration_number, colormap):
        """
        The actual code on this is based upon the Wikipedia pseudocode.

        :param x_pixels: The range for the np.linspace function for x coordinates.
                         The more pixels, the better the mandelbrot will look.

        :param y_pixels: The range for the np.linspace function for y coordinates.
                         The more pixels, the better the mandelbrot will look.

        :param power_z: The power of z. For mandelbrot: enter 2, for some other interesting patterns,
                        just type anything else.

        :param iteration_number: The number of iterations for the rendering. This is just to check the
                                 convergence of the set.

        :param colormap: A matplotlib colormap that you can enter.
        :return:
        """
        px = np.linspace(-2, 2, x_pixels) # X axis
        py = np.linspace(-2, 2, y_pixels) # Y axis
        max_z = 2 # Check if the value is greater than this

        iterations = [] # List of the result calculations

        for y in py:                                 # For every y in the max amount of y pixels
            row = []                                 # List of the result of y coordinate
            for x in px:                             # For every x in the max amount of x pixels
                c = complex(x, y)                    # Complex number c in the form of x + yi
                z = 0                                # Initial value for the iteration
                for i in range(1, iteration_number): # Runs loop from 1 to the max amount of iterations
                    if abs(z) >= max_z:              # If |z| is greater than 2, it is considered to diverge
                        row.append(i)                # Number of iterations it took to escape(for coloring)
                        break                        # Breaks loop because the number has already diverged
                    else:
                        z = (z ** power_z) + c       # Makes new value of z
                else:
                    row.append(0)                    # This means the point converges, and so belongs to the fractal.

            iterations.append(row) # Append the row to the final list. This is the list we plot the fractal in!

        axis = plt.axes()
        axis.set_aspect('equal')
        plt.colorbar(axis.pcolormesh(px, py, iterations, cmap=colormap)) # Colormap
        plt.xlabel("Real Axis")
        plt.ylabel("Imaginary Axis")
        plt.show() # Plotting the fractal

    # Inputs
    x_pixels = int(input("How many pixels for real axis? "))
    y_pixels = int(input("How many pixels for imaginary axis? "))
    power_z = int(input("What would be the power of z? "))
    iteration_number = int(input("How many iterations for the fractal? "))
    colormap = input("Please write a valid matplotlib colormap for the render: ")

    # Calling the function
    render(x_pixels, y_pixels, power_z, iteration_number, colormap)


def nt_problems():
    """
    Some functions on number theory. For more help with the actual functions, please do call the respective
    functions themselves. The two problems we have here are:
    --------------------------
    1. Perfect Number Searcher
    2. Mersenne Prime Searcher
    --------------------------
    :return:
    """
    def is_prime(num):
        """
        This is a very fast way to check if a number is prime, rather than just checking using the Sieve of
        Eratosthenes. You can just set the upper range to be the square root of the number, since there will
        be no factors greater than the square root of the number if the number does happen to be a prime.
        :param num:
        :return:
        """
        x = 0
        for i in range(1, int(math.sqrt(num)) + 1): # Fast method to check if a number is prime
            if num % i == 0:
                x += 1

        if x == 2:
            return True
        else:
            return False

    def search_pn(n):
        """
        A perfect number is that number that is equal to the sum of it's divisors. An example of a perfect
        number is:

        =====================
        6 = 3 + 2 + 1
        =====================

        The first few perfect numbers are 6, 28, 496, 8128, ...
        For this, I just implemented a quick way to get all the sums of the factors, by only iterating through
        the first n/2 terms, because there are no proper factors of a number that is greater than the number
        divided by 2.

        :param n: The limit for the search of the perfect number.
        :return:
        """
        for k in range(2, n):
            x = 0 # Sum of the factors
            for i in range(1, int(k / 2) + 1): # Go through the factors of k
                if k % i == 0: # Is i a factor of k?
                    x += i # Get the sum of the factor

            if x == k: # If the sum of the divisors is equal to the actual number.
                print(f'YES! {k} is a perfect number!')

    def search_mersenne(n):
        """
        A Mersenne Prime is any prime number that can be represented in the way: 2^p-1, where p is also
        another prime number. Here I just did a typical brute force method to find the Mersenne Primes,
        although a way faster method would be to implement the Sieve of Eratosthenes.

        :param n: The limit for the search of the Mersenne Prime.

        :return:
        """
        for i in range(1, n):
            if is_prime(i): # Is the number prime?
                possible = (2 ** i - 1) # The form of a Mersenne Prime
                if is_prime(possible): # Is the number we formed a Mersenne Prime?
                    print(f'{i} is a Mersenne prime!')

    # Printing the options

    print("1. Perfect Number Searcher")
    time.sleep(.5)
    print("2. Mersenne Prime Searcher")
    time.sleep(.5)
    print()
    print()
    time.sleep(.5)
    choose = input("Type out which one you would like to use: ").lower()

    # Conditions

    if choose[0] == 'p':
        # Taking the required input
        n = int(input("Enter maximum limit for the Perfect Number Search: "))
        search_pn(n)
        done = True
    elif choose[0] == 'm':
        # Taking the required input
        n = int(input("Enter maximum limit for the Mersenne Prime Search: "))
        search_mersenne(n)
        done = True
    else:
        # Invalid input case(reloads the program)
        print("Sorry! You have an invalid input.")
        time.sleep(1)
        print("Program reloading...")
        time.sleep(.5)
        nt_problems()
        done = False

    if done:
        sys.exit() # Closes the program
    else:
        nt_problems() # Recall the program if the user input an invalid option.


def calc():
    """
    A graphing calculator inspired by Desmos. There are 6 options:
    ============================================================
    1. Trigonometric Functions
    2. Linear Functions
    3. Quadratic Functions
    4. Cubic Functions
    5. Logarithmic Functions
    6. Plotting in 3 Dimensions
    ============================================================
    Choosing any one of these will lead you to another function defined that will give you the necessary
    inputs to graph the actual thing.
    :return:
    """
    def main():
        """
        The main function for the graphing calculator. I will explain each one of the functions that I have
        implemented into this code.
        ============================
        1. Trigonometric Functions:
            Uses scipy library for the normal trigonometric functions, but I used matplotlib to graph the
            hyperbolic functions as when I was first doing the code, I just messed around with matplotlib
            a bit. With matplotlib and numpy, I made an array of coordinates using np.arange and I plotted
            each one of those coordinates, and it's respective output. For sympy there is just a simple
            syntax to actually print out the graph.
        ============================
        2. Linear Functions:
            Uses sympy to plot the straight line. Here I just made the user input the values of the constants
            in the function of the straight line, then used some simple sympy syntax to graph the line.
        ============================
        3. Quadratic Functions:
            Uses sympy to plot the parabola. I got the user to input the coefficients in the function and
            the constant. I then used some simple sympy syntax to print out the parabola's graph.
        ============================
        4. Cubic Functions:
            Uses sympy to plot the cubic graph. This part gets input from the user, asking for the coefficients
            of the cubic function, then puts them all together using some sympy plot() syntax, and then it will
            print out the graph.
        ============================
        5. Logarithmic Functions:
            There are two options for this:
            a) log_n(x):
                Asks the user for a base 'n', and will show the logarithmic graph using sympy.
            b) ln(x):
                Shows the natural logarithm graph using sympy.
        ============================
        6. 3 Dimensional Plotting
            Uses the library sympy to ask the user for some 3D Plotting choices, and it will plot the
            actual 3D graph. This one can't really be customized, as I did not want to go through the
            trouble of making a customized 3D Plotter.
        ============================
        :return:
        """

        x_coord = []
        y_coord = []
        x = symbols('x')

        # Printing the menu

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
            # Options
            print("__________________TRIGONOMETRY_______________________")
            print("|1. sinh(x)|2. cosh(x)|3. tanh(x)|")
            print("|4. sin(x) |5. cos(x) | 6. tan(x)|")
            print("----------------------------------------------------")
            print("----------------------------------")
            trig_pick = int(input("Pick any from 1-6: ")) # Take user input
            if trig_pick == 1:
                # Generate the coordinates
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.sinh(n)) # Y coordinate value calculation
                    x_coord.append(i)

                plt.plot(x_coord, y_coord) # Plot the coordinates
                plt.show() # Show the plot
            elif trig_pick == 2:
                # Generate the coordinates
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.cosh(n)) # Y coordinate value calculation
                    x_coord.append(i)

                plt.plot(x_coord, y_coord) # Plot the coordinates
                plt.show() # Show the plot
            elif trig_pick == 3:
                # Generate the coordinates
                for i in np.arange(-5, 5, 0.5):
                    n = i
                    y_coord.append(math.tanh(n)) # Y coordinate value calculation
                    x_coord.append(i)

                plt.plot(x_coord, y_coord) # Plot the coordinates
                plt.show() # Show the plot
            elif trig_pick == 4:

                plot(sin(x), (x, -7.5, 7.5), ylim=(-1.5, 1.5), xlabel="x", ylabel="y")
                # Plot the sin(x) graph

            elif trig_pick == 5:

                plot(cos(x), (x, -7.5, 7.5), ylim=(-1.5, 1.5), xlabel="x", ylabel="y")
                # Plot the cos(x) graph

            elif trig_pick == 6:

                plot(tan(x), (x, -10, 10), ylim=(-20, 20), xlabel="x", ylabel="y")
                #Plot the tan(x) graph

            else:
                # Invalid input case
                print("Invalid Input! Please try again.")
                main()

        elif inp[1] == 'i':
            print("---------------LINEAR FUNCTION-------------------")
            print("-------------------ax + b------------------------")
            time.sleep(.5)
            # Input the coefficients
            linear_a = int(input("a: "))
            linear_b = int(input("b: "))
            print("-------------------------------------------------")
            plot((linear_a * x + linear_b), (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")
            #           ^ This part will combine the coefficients to give a function in the form ax + b.
        elif inp[0] == 'q':
            print("--------------QUADRATIC FUNCTION-----------------")
            print("----------------ax^2 + bx + c--------------------")
            time.sleep(.5)
            # Input the coefficients
            quad_a = int(input("a: "))
            quad_b = int(input("b: "))
            quad_c = int(input("c: "))
            print("-------------------------------------------------")
            plot((quad_a * x ** 2 + quad_b * x + quad_c), (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")
            #           ^ This part will combine the coefficients to give a function in the form ax^2 + bx
            #             + c.
        elif inp[0] == 'c':
            print("---------------------CUBIC FUNCTION--------------------")
            print("-----------------ax^3 + bx^2 + cx + d------------------")
            time.sleep(.5)
            # Input the coefficients
            cubic_a = int(input("a: "))
            cubic_b = int(input("b: "))
            cubic_c = int(input("c: "))
            cubic_d = int(input("d: "))
            print("-------------------------------------------------------")
            plot((cubic_a * x ** 3 + cubic_b * x ** 2 + cubic_c * x + cubic_d), (x, -10, 10), ylim=(-10, 10),
                 xlabel="x", ylabel="y")
            # The above part will combine the coefficients to give a function in the form of ax^3 + bx^3 +
            # cx + d.
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
                log_eqn = ln(x) # The equation for the logarithm
            elif ln_log[0] == 'l':
                base = int(input("Logarithm Base(a): "))
                log_eqn = log(x, base) # The equation for the logarithm
            else:
                # Invalid input case
                print("Invalid Input! Please try again.")
                main()

            plot(log_eqn, (x, -10, 10), ylim=(-10, 10), xlabel="x", ylabel="y")
            # Plotting the actual logarithm.

        elif inp[0] == '3':
            print("---------------3 DIMENSIONAL PLOTTING------------------")
            time.sleep(.5)
            print("-------------------------------------------------------")
            # Options for the 3D Plotting
            print("1. z = x*y")
            print("2. z = x/y")
            print("3. z = cos(x), z = sin(x), z = x")
            print("4. z = cos(x + y), z = sin(x + y), z = x + y")
            print("5. z = x^2 + y^2")
            u, v = symbols("u v")

            input3d = int(input("Choose from 1-5: "))
            if input3d == 1:
                plot3d((u * v, (u, -5, 5), (v, -5, 5))) # Plot the first function
            elif input3d == 2:
                plot3d((u / v, (u, -5, 5), (v, -5, 5)))# Plot the second function
            elif input3d == 3:
                plot3d_parametric_line((cos(u), sin(u), u, (u, -5, 5)),
                                       (sin(u), u ** 2, u, (u, -5, 5))) # Plot the third function
            elif input3d == 4:
                plot3d_parametric_surface(cos(u + v), sin(u - v), u - v,
                                          (u, -5, 5), (v, -5, 5)) # Plot the fourth function
            elif input3d == 5:
                plot3d((u ** 2 + v ** 2, (u, -5, 5), (v, -5, 5))) # Plot the fifth function
            else:
                # Invalid input case
                print("Invalid Input! Please try again.")
                main()
        else:
            # Invalid input case
            print("Invalid Input! Please try again.")
            main()

    main() # Call the graphing calculator


def maclaurin():
    """
    This is a function that will give you three options:
    --------------------------
    1. sin(x) 2. cos(x) 3. e^x
    --------------------------
    Choose your desired option from here, and the respective functions defined here will graph the visualization
    of the Maclaurin Series using matplotlib.

    :return:
    """
    def e_power_x(x, n):
        """
        This is just the definition of the exponential function, it's very easy. If you do not understand this,
        I'd recommend you catch up to this using some article or videos.
        :param x: The x coordinates, given from -pi to +pi with a difference of 0.05.
        :param n: The number of iterations for the Taylor Series.
        :return:
        """
        taylor_approximation = 0
        for i in range(0, n):
            taylor_approximation += (x ** i) / math.factorial(i)

        return taylor_approximation

    def f_sin(x, n):
        """
        Definition of the Taylor Series expansion of sin(x). If you took Calculus 2 you could easily understand
        this code, otherwise I would suggest you to catch up on some articles relating to this matter.
        :param x: The x coordinates from -pi to +pi, with a difference of 0.05
        :param n: The number of iterations for the Taylor Series
        :return:
        """
        taylor_approximation = 0
        for i in range(1, n):
            taylor_approximation += (-1) ** (i - 1) * (x ** (2 * i - 1) / math.factorial(2 * i - 1))
        return taylor_approximation

    def f_cos(x, n):
        """
        This is the definition for the Taylor Series expansion of cos(x). If you have taken Calculus 2, you
        could easily be able to understand this, if not, I recommend you look up some articles explaining it.
        :param x: The x coordinates, that is given from -pi to +pi with a difference of 0.05 in between.
        :param n: The number of iterations for the actual expansion
        :return:
        """
        taylor_approximation = 0
        for i in range(n):
            taylor_approximation += (-1) ** i * (x ** (2 * i) / math.factorial(2 * i))
        return taylor_approximation

    print("----------------------------------")
    print("| 1. sin(x) | 2. cos(x) | 3. e^x |")
    print("----------------------------------")
    time.sleep(.5)

    taylor_input = input("Choose a function to approximate: ") # User can choose any option

    if taylor_input[0] == 's':

        iterations = int(input("How many iterations for the Taylor Series? ")) # Asks for the iterations

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05) # The set of x coordinates
        sine = np.sin(x_range) # Calculating the sine function

        figure, axes = plt.subplots()
        axes.plot(x_range, sine, color='black', linewidth=3) # Plotting the sine function
        for i in range(1, iterations + 1):
            taylor_sine = [f_sin(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_sine) # Plotting the approximation

        axes.set_ylim([-3, 3])
        legend = ['sin(x)']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of sin(x): {i} iterations')

        axes.legend(legend)
        plt.show() # Show the plot

    elif taylor_input[0] == 'c':

        iterations = int(input("How many iterations for the Taylor Series? ")) # Asks for the iterations

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05) # The set of x coordinates
        cosine = np.cos(x_range) # Cosine function

        figure, axes = plt.subplots()
        axes.plot(x_range, cosine, color='black', linewidth=3) # Plotting the cosine function
        for i in range(1, iterations + 1):
            taylor_cosine = [f_cos(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_cosine) # Plotting the approximation

        axes.set_ylim([-3, 3])

        legend = ['cos(x)']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of cos(x): {i} iterations')

        axes.legend(legend)
        plt.show() # Show the plot

    elif taylor_input[0] == 'e':

        iterations = int(input("How many iterations for the Taylor Series? ")) # Asks for the iterations

        x_range = np.arange(-2 * np.pi, 2 * np.pi, 0.05)
        e_x = np.exp(x_range) # Exponential function

        figure, axes = plt.subplots()
        axes.plot(x_range, e_x, color='black', linewidth=3) # Plot the exponential function
        for i in range(1, iterations + 1):
            taylor_e = [e_power_x(x_coords, i) for x_coords in x_range]
            axes.plot(x_range, taylor_e) # Plot the approximation

        axes.set_ylim([-3, 3])

        legend = ['e^x']
        for i in range(1, iterations + 1):
            legend.append(f'Maclaurin/Taylor series of e^x: {i} iterations')

        axes.legend(legend)
        plt.show() # Show the plot


def wpm():
    """
    This is a quick program that I made, it measures your words per minute. As said, it is a very quick program,
    so it is really not that accurate. I just used some logic, and it calculates your average wpm, doesn't
    count accuracy, or your actual speed. It just uses a simple formula that I made up, so your words per
    minute should be a little higher than the one you see here. It has around 70 common words in the list.
    =======================
    INSPIRED BY MONKEYTYPE
    =======================
    :return:
    """
    list = [
        'also', 'during', 'find', 'be', 'on', 'work', 'or', 'school', 'line', 'just', 'number',
        'any', 'become', 'many', 'do', 'as', 'both', 'down', 'hold', 'it', 'he', 'could', 'she',
        'become', 'who', 'present', 'any', 'when', 'into', 'no', 'and', 'how', 'help', 'leave',
        'know', 'face', 'will', 'way', 'govern', 'can', 'each', 'form', 'fact', 'system', 'ask',
        'very', 'of', 'make', 'work', 'program', 'eye', 'than', 'head', 'hand', 'would', 'give',
        'but', 'day'
    ]
    chosen_words = ""

    print("1. 10 Words")
    print("2. 30 Words")
    print("3. 50 Words")

    user_input = str(input("Enter which one you want to do: "))
    print()
    if user_input[0] == '1':

        # This gets 10 random words

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
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 600 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '3':
        for i in range(1, 31):

            # This gets 30 random words

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
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 1800 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')

    elif user_input[0] == '5':
        for i in range(1, 51):

            # This gets 50 random words

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
        str(input(""))
        end = time.time()
        length = end - start
        wpm = 3000 / length # Calculation

        # Shows your words per minute
        print(f'You have {wpm} words per minute.')


def center_window(window):

    """
    This is a way to center the menu in TKinter. I found it on stackoverflow, and it's really useful. Basically,
    what it does is it grabs your screen width and height, gets the window width and height, subtracts
    them, divides by 2 to get the middle point, and that is how you center the window.

    :param window: The window that you are working on(TKinter)
    :return:
    """

    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")


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
