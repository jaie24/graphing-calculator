# import necessary libraries
from math import *
import turtle

# Constants
BACKGROUND_COLOR = "white"
WIDTH = 800
HEIGHT = 600
AXIS_COLOR = "black"
INCREMENT = 1
DELTA = 0.1
PRIMARY_OFFSET = 3
SECONDARY_OFFSET = 15


def get_color(equation_counter):
    """
    Get color for an equation based on counter of how many equations have been drawn (this is the xth equation)
    :param equation_counter: Number x, for xth equation being drawn
    :return: A string color for turtle to use
    """

    # function returns either one of these three colours : red, green or blue

    if (equation_counter % 3) == 0:
        return "red"

    elif (equation_counter % 3) == 1:
        return "green"

    else:
        return "blue"


def calc_to_screen_coord(x, y, x_origin, y_origin, ratio):
    """
    Convert a calculator (x,y) to a pixel (screen_x, screen_y) based on origin location and ratio
    :param x: Calculator x
    :param y: Calculator y
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (screen_x, screen_y) pixel version of calculator (x,y)
    """

    # this function returns the x and y coordinate as screen coordinates below
    # screen_x = x coordinate and screen_y = y coordinate

    screen_x = x_origin + ( ratio * x )
    screen_y = y_origin + (ratio * y)
    return screen_x, screen_y


def calc_minmax_x(x_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER x value to draw for a 0->WIDTH of screen
    Smallest: Convert a pixel x=0 to a calculator value and return integer floor
    Largest : Convert a pixel x=WIDTH to a calculator value and return integer ceiling
    :param x_origin: Pixel x origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) x value to draw for a 0->WIDTH of screen
    """
    # Smallest Calculator Coordinate when Pixel X = 0
    smallest_x = ((0 - x_origin) / ratio)
    min_x = int(floor(smallest_x))

    # Largest Calculator Coordinate for X = WIDTH
    largest_x = ((WIDTH - x_origin) / ratio)
    max_x = int(ceil(largest_x))

    return min_x, max_x


def calc_minmax_y(y_origin, ratio):
    """
    Calculate smallest and largest calculator INTEGER y value to draw for a 0->HEIGHT of screen
    Smallest: Convert a pixel y=0 to a calculator value and return integer floor
    Largest : Convert a pixel y=HEIGHT to a calculator value and return integer ceiling
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: (Smallest, Largest) y value to draw for a 0->HEIGHT of screen
    """
    # Smallest Calculator Coordinate when Pixel Y = 0
    smallest_y = ((0 - y_origin) / ratio)
    min_y = int(floor(smallest_y))

    # Largest Calculator Coordinate for Y = HEIGHT
    largest_y = ((HEIGHT - y_origin) / ratio)
    max_y = int(ceil(largest_y))

    return min_y, max_y


def draw_line(pointer, screen_x1, screen_y1, screen_x2, screen_y2):
    """
    Draw a line between two pixel coordinates (screen_x_1, screen_y_1) to (screen_x_2, screen_y_2)
    :param pointer: Turtle pointer to draw with
    :param screen_x1: The pixel x of line start
    :param screen_y1: The pixel y of line start
    :param screen_x2: The pixel x of line end
    :param screen_y2: The pixel y of line end
    :return: None (just draws in turtle)
    """

    # To draw a line, pointer needs to start from one point and go to another point
    # screen_x1, screen_y1 represents one point
    # screen_x2, screen_y2 represents another point
    # pointer then draws from screen_x1, screen_y1 to screen_x2, screen_y2

    pointer.goto(screen_x1, screen_y1)
    pointer.down()
    pointer.goto(screen_x2, screen_y2)
    pointer.up()


def draw_x_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an x-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.color("black")
    # draw the line
    # constant PRIMARY_OFFSET is implemented here whereby it is an offset of 3
    draw_line(pointer, screen_x, screen_y - PRIMARY_OFFSET, screen_x, screen_y + PRIMARY_OFFSET)
    pointer.up()


def draw_x_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an x-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.color("black")
    # a different constant SECONDARY_OFFSET is implemented here whereby it is an offset of 15
    pointer.goto(screen_x,screen_y - SECONDARY_OFFSET)
    pointer.write(label_text)


def draw_y_axis_tick(pointer, screen_x, screen_y):
    """
    Draw an y-axis tick for location (screen_x, screen_y)
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :return: None (just draws in turtle)
    """
    pointer.color("black")
    # constant PRIMARY_OFFSET = 3 is implemented here again
    draw_line(pointer, screen_x - PRIMARY_OFFSET, screen_y, screen_x + PRIMARY_OFFSET, screen_y)
    pointer.up()



def draw_y_axis_label(pointer, screen_x, screen_y, label_text):
    """
    Draw an y-axis label for location (screen_x, screen_y), label is label_text
    :param pointer: Turtle pointer to draw with
    :param screen_x: The pixel x of tick location on axis
    :param screen_y: The pixel y of tick location on axis
    :param label_text: The string label to draw
    :return: None (just draws in turtle)
    """
    pointer.color("black")
    # constant SECONDARY_OFFSET = 15 is implemented
    # constant PRIMARY_OFFSET = 3 is also implemented here
    pointer.goto(screen_x - SECONDARY_OFFSET, screen_y - PRIMARY_OFFSET)
    pointer.write(label_text)



def draw_x_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an x-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    # Set the Colour of the Axis
    pointer.color("black")

    # First Get the Minimum Value of X and Maximum of X to for the start and end of the line by calling the function
    # calc_minmax_x function returns the min x and max x in calculator coordinates
    minimum_value_x, maximum_value_x = calc_minmax_x(x_origin, ratio)

    # along the x-axis, screen_coord_x1 is at min x in calc coordinates, while y is at origin or 0 in calc coordinates.
    # therefore, convert the calculator coordinates to screen coordinates to draw the axis
    # call the calc_to_screen_coord function to convert the coordinates
    screen_coord_x1, screen_coord_y1 = calc_to_screen_coord(minimum_value_x, 0, x_origin, y_origin, ratio)
    screen_coord_x2, screen_coord_y2 = calc_to_screen_coord(maximum_value_x, 0, x_origin, y_origin, ratio)

    # now draw the line of the x-axis by calling the draw line function
    draw_line(pointer, screen_coord_x1, screen_coord_y1, screen_coord_x2, screen_coord_y2)

    # now draw the ticks and labels
    # we will start with ticks then labels
    # implement the loop

    for coordinate_x in range(minimum_value_x, maximum_value_x + INCREMENT, INCREMENT):
        screen_coord_x1, screen_coord_y1 = calc_to_screen_coord(coordinate_x, 0, x_origin, y_origin, ratio)
        draw_x_axis_tick(pointer, screen_coord_x1, screen_coord_y1)
        draw_x_axis_label(pointer, screen_coord_x1, screen_coord_y1, coordinate_x)


def draw_y_axis(pointer, x_origin, y_origin, ratio):
    """
    Draw an y-axis centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """

    # Set the Colour of the Axis
    pointer.color("black")

    # First Get the Minimum Value of Y and Maximum of Y to for the start and end of the line by calling the function
    # calc_minmax_y function returns the min y and max y in calculator coordinates
    minimum_value_y, maximum_value_y = calc_minmax_y(y_origin, ratio)

    # along the y-axis, screen_cord_x1 is at x origin, which in calculator coordinates is 0. and screen_coord_y1 is min y
    # therefore, convert the calculator coordinates to screen coordinates to draw the axis
    # call the calc_to_screen_coord function to convert the calc coordinates to screen coordinates
    screen_coord_x1, screen_coord_y1 = calc_to_screen_coord(0, minimum_value_y, x_origin, y_origin, ratio)
    screen_coord_x2, screen_coord_y2 = calc_to_screen_coord(0, maximum_value_y, x_origin, y_origin, ratio)

    # now draw the line of the y-axis by calling draw_line function
    draw_line(pointer, screen_coord_x1, screen_coord_y1, screen_coord_x2, screen_coord_y2)

    # now draw the ticks and labels
    # we will start with ticks then labels
    # implement the loop

    for coordinate_y in range(minimum_value_y, maximum_value_y + INCREMENT, INCREMENT):
        screen_coord_x2, screen_coord_y2 = calc_to_screen_coord(0, coordinate_y, x_origin, y_origin, ratio)
        draw_y_axis_tick(pointer, screen_coord_x2, screen_coord_y2)
        draw_y_axis_label(pointer,screen_coord_x2,screen_coord_y2,coordinate_y)


def draw_expression(pointer, expr, colour, x_origin, y_origin, ratio):
    """
    Draw expression centred on given origin, with given ratio
    :param pointer: Turtle pointer to draw with
    :param expr: The string expression to draw
    :param colour: The colour to draw the expression
    :param x_origin: Pixel x origin of pixel coordinate system
    :param y_origin: Pixel y origin of pixel coordinate system
    :param ratio: Ratio of pixel coordinate system (each 1 in calculator is worth ratio amount of pixels)
    :return: None (just draws in turtle)
    """
    pointer.color(colour)
    # Implement Min and Max X for range later on
    # Min and Max X is to set the range of where x coordinates will be drawn
    # Returns Min and Max X in Calculator Coordinates
    minimum_value_x, maximum_value_x = calc_minmax_x(x_origin, ratio)
    # do the same for min and max y if expressions outside the window is eliminated
    # MinimumValueOfY, MaximumValueOfY = calc_minmax_y(y_origin, ratio)

    # Assign a starting point for drawing the line
    # Starting point of x starts at Minimum Value of X
    # For a smoother curve, DELTA is used.
    # DELTA = 0.1 is a constant and has been implemented at the top of the code.

    x = minimum_value_x
    while x <= maximum_value_x:
        x1 = x
        x2 = x + DELTA
        y1 = calc(expr, x1)
        y2 = calc(expr, x2)

        # Convert the calculator coordinates of the two points into screen coordinates
        screen_coordinate_x1, screen_coordinate_y1 = calc_to_screen_coord(x1, y1, x_origin, y_origin, ratio)
        screen_coordinate_x2, screen_coordinate_y2 = calc_to_screen_coord(x2, y2, x_origin, y_origin, ratio)

        # Once the screen coordinates are obtained, draw_line function is implemented to draw the lines
        draw_line(pointer, screen_coordinate_x1, screen_coordinate_y1, screen_coordinate_x2, screen_coordinate_y2)

        # X coordinate is updated with DELTA. Once it reaches max value of x, the loop stops.
        x += DELTA


def calc(expr, x):
    """
    Return y for y = expr(x)
    Example if x = 10, and expr = x**2, then y = 10**2 = 100.
    :param expr: The string expression to evaluate where x is the only variable
    :param x: The value to evaluate the expression at
    :return: y = expr(x)
    """

    return eval(expr)


def setup():
    """
    Sets the window up in turtle
    :return: None
    """
    turtle.bgcolor(BACKGROUND_COLOR)
    turtle.setup(WIDTH, HEIGHT, 0, 0)
    screen = turtle.getscreen()
    screen.screensize(WIDTH, HEIGHT)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    screen.delay(delay=0)
    pointer = turtle
    pointer.hideturtle()
    pointer.speed(0)
    pointer.up()
    return pointer


def main():
    """
    Main loop of calculator
    Gets the pixel origin location in the window and a ratio
    Loops a prompt getting expressions from user and drawing them
    :return: None
    """
    # Setup
    pointer = setup()
    # turtle.tracer(0)
    # Get configuration
    x_origin, y_origin = eval(input("Enter pixel coordinates of chart origin (x,y): "))
    ratio = int(input("Enter ratio of pixels per step: "))
    # Draw axis
    pointer.color(AXIS_COLOR)
    draw_x_axis(pointer, x_origin, y_origin, ratio)
    draw_y_axis(pointer, x_origin, y_origin, ratio)
    # turtle.update()
    # Get expressions
    expr = input("Enter an arithmetic expression: ")
    equation_counter = 0
    while expr != "":
        # Get colour and draw expression
        colour = get_color(equation_counter)
        draw_expression(pointer, expr, colour, x_origin, y_origin, ratio)
        # turtle.update()
        expr = input("Enter an arithmetic expression: ")
        equation_counter += 1


main()
turtle.exitonclick()
