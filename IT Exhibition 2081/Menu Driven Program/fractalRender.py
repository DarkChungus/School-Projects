import numpy as np
import matplotlib.pyplot as plt

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
