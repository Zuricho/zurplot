import matplotlib.pyplot as plt




def draw_fraction(numerator, denominator, x, y, fontsize=12, color="tab:blue"):
    """
    Draws a fraction at a given position (x, y) on the plot using plt.* functions,
    adjusting the line width based on the width of the numerator or denominator.
    
    :param numerator: Numerator of the fraction
    :param denominator: Denominator of the fraction
    :param x: x-coordinate on the plot
    :param y: y-coordinate on the plot
    :param fontsize: Font size of the fraction text
    """
    # Convert numerator and denominator to strings
    num_str = str(numerator)
    denom_str = str(denominator)

    # Estimate text width and use it to set line width
    max_text_width = max(len(num_str), len(denom_str))
    line_width = fontsize * max_text_width * 0.012  # Scale line width with text size and length

    # Get current y-axis limits to calculate relative offset
    y_min, y_max = plt.ylim()
    y_range = y_max - y_min
    offset = y_range * 0.01  # 2% of the y-axis range

    # Draw numerator and denominator with adjusted vertical spacing
    plt.text(x, y + offset, num_str, fontsize=fontsize, ha='center', va='bottom', color=color)
    plt.text(x, y - offset, denom_str, fontsize=fontsize, ha='center', va='top', color=color)

    # Draw line
    plt.gca().add_line(plt.Line2D([x - line_width/2, x + line_width/2], [y, y], lw=1, color=color))



