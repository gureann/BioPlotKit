from matplotlib import pyplot as plt


def remove_all_axis(ax=None):
    if ax is None:
        ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    for _ in ['top', 'right', 'bottom', 'left']:
        ax.spines[_].set_visible(False)
