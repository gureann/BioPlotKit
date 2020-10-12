import pandas as pd
import matplotlib.pyplot as plt

from bioplotkit.drawing_area import set_thousand_separate


def count_bar(data,
              ylim=None, xlim=None,
              bar_width=0.6, bar_color=None,
              xlabel='Missed cleavage', ylabel='Number of peptides',
              title='',
              ax=None):
    if ax is None:
        ax = plt.gca()

    if isinstance(data, list):
        ser = pd.Series(dict(data))
    elif isinstance(data, dict):
        ser = pd.Series(data)
    elif isinstance(data, pd.Series):
        ser = data
    else:
        raise TypeError
    ser = ser.sort_index()

    list_data = list(ser.items())

    ax.bar(*list(zip(*list_data)), width=bar_width, color=bar_color)
    for idx, num in list_data:
        ax.annotate(format(num, ','), (idx, num / 2), ha='center')

    set_thousand_separate(ax, 'y')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
