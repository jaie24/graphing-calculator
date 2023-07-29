# graphing-calculator
a simple graphing calculator that draws the result of an expression on the window
Description: 
- The program firstly prompts the user for the origin in pixel coordinates, ratio of pixels each step and the arithmetic expression.
- The program calls several functions.
- When the user inputs the expression, the axis is drawn in black using the functions draw_x_axis, calc_minmax_x, draw_line, draw_x_axis_tick and draw_axis_label
- The same is done for the y-axis by calling functions : draw_y_axis, calc_minmax_y, draw_line, draw_y_axis_tick and draw_y_axis label
- To display the result of the arithmetic expression on the turtle window, the program calls the draw_expression function and get_color function
- The color of the expressions depends on the number of expression that the user inputs, which results in either red, green or blue respectively.
