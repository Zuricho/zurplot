import matplotlib as mpl



# colormaps for matplotlib
cmap_color_list = [
    # "#F5F263",
    "#81D152",
    "#42ADC7",
    "#5B4DB7",
]


cmap_zuricho = mpl.colors.LinearSegmentedColormap.from_list("zuricho_cmap", cmap_color_list, N=120)


