from typing import Union

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from zurplot.utils import draw_fraction


def bar(
    height: Union[list, np.ndarray],
    xticks: Union[list, np.ndarray],
    ylabel: str = None,
    width: float = 0.8,
    color: Union[str, list, np.ndarray] = "tab:blue",
    alpha: float = 0.8,
    edgecolor: str = "#222222",
    xticks_rotation: int = 90,
    numerator: Union[list, np.ndarray] = None,
    denominator: Union[list, np.ndarray] = None,
    yaxis_percentage: bool = False,
):
    """Barplot

    Args:
        height (Union[list, np.ndarray]): height of the bar
        xticks (Union[list, np.ndarray]): xticks
        ylabel (str): ylabel
        width (float, optional): width of the bar. Defaults to 0.8.
        color (Union[str, list, np.ndarray], optional): color of the bar. Defaults to "tab:blue".
        alpha (float, optional): alpha of the bar. Defaults to 0.8.
        edgecolor (str, optional): edgecolor of the bar. Defaults to "#222222".
        xticks_rotation (int, optional): rotation of xticks. Defaults to 90.
        numerator (Union[list, np.ndarray], optional): numerator of the fraction. Defaults to None.
        denominator (Union[list, np.ndarray], optional): denominator of the fraction. Defaults to None.
    
    Example:
        bar(
            height=[0.1, 0.2, 0.3],
            xticks=["a", "b", "c"],
            ylabel="ylabel",
            width=0.8,
            color="tab:blue",
            alpha=0.8,
            edgecolor="#222222",
            xticks_rotation=90,
            numerator=None,
            denominator=None,
        )
    """
    plt.bar(
        x=np.arange(len(height)), 
        height=height,
        width=width,
        color=color,
        alpha=alpha,
        edgecolor=edgecolor)

    # text
    if numerator is not None and denominator is not None:
        for i in np.arange(len(height)):
            draw_fraction(numerator[i], denominator[i], i, height[i]+max(height)*0.08, fontsize=10, color=edgecolor)
    else:
        for i in np.arange(len(height)):
            plt.text(i, height[i]+max(height)*0.05, f"{height[i]}", ha="center", va="center", fontsize=10, color=edgecolor)


    # parameters
    plt.xlim(-0.6, len(height)-0.4)
    plt.ylim(0, max(height)*1.2)
    plt.xticks(np.arange(0,len(height)-0.1,1), xticks, rotation=xticks_rotation, fontweight="bold", rotation_mode="anchor", ha="right")
    plt.ylabel(ylabel, fontweight="bold", fontsize=14)
    # convert to percentage
    if yaxis_percentage:
        plt.gca().yaxis.set_major_formatter(mpl.ticker.PercentFormatter(xmax=1))


