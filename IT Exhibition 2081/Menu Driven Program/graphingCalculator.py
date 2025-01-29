import matplotlib.pyplot as plt
import math
import numpy as np
from sympy import *
from sympy.plotting import plot3d
from sympy.plotting import plot3d_parametric_surface
from sympy.plotting import plot3d_parametric_line
import time

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
