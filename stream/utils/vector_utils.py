import matplotlib.pyplot as plt


def plot_vector(
    x_bounds: "tuple[int, int]",
    y_bounds: "tuple[int, int]",
    vector: "list[int, int]",
    color="b",
) -> None:
    """Function for plotting a magnetic vector relative to the current window size

    x_bounds: tuple of plot bounds in the form of (min, max)
    y_bounds: tuple of plot bounds in the form of (max, min)
    vector: unit vector in the form of [x, y]
    color: default color of plotted vector"""
    # print(x_bounds, y_bounds) # debugging print statement

    axis_len = None  # len of shortest axis

    # checks if height < width; the shorter axis is used for subsequent calculations
    if (y_bounds[0] - y_bounds[1]) < (x_bounds[1] - x_bounds[0]):
        axis_len = y_bounds[0] - y_bounds[1]
    else:
        axis_len = x_bounds[1] - x_bounds[0]

    # Plot vector according the the shorter axis. Origin point is situated at
    # the top right of the window, offset by 1/14 of the shorter axis length.
    # Scale adjusted to be 1/25 of the shorter axis length.
    x_origin = x_bounds[1] - axis_len / 14  # x coordinate of the vector's origin point
    y_origin = y_bounds[1] + axis_len / 14  # y coordinate of the vector's origin point
    scale = axis_len / 25  # number of data units per arrow length

    # plots vector originating from the designated origin
    plt.quiver(x_origin, y_origin, vector[0], vector[1], color=color, scale=scale)
