import matplotlib.pyplot as plt
import time
import math
import numpy as np

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
