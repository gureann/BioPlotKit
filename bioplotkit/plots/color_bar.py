

def color_bar(two_side, show_tick, figure_direct, anno_loc, ax):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    colors = heatmap_color_bar
    n = len(colors)
    for i, c in enumerate(colors):
        ax.plot((i / n, i / n), (0, 1), color=c)

    for anno_index, anno in enumerate(['-2', '0', '2']):
        ax.annotate(anno, (anno_index / 2, 1),
                     textcoords='offset points', xytext=(0, 0.25),
                     va='bottom', ha='center', fontsize=FontSize_Small, rotation=0)

    ax.annotate('z-score intensity', (0.5, 1),
                 textcoords='offset points', xytext=(0., 7.),
                 va='bottom', ha='center', fontsize=FontSize_Small, rotation=0)

