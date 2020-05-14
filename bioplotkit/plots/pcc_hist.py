from bioplotkit.drawing_area.ax_utls import set_thousand_separate

from matplotlib import pyplot as plt
import numpy as np


def pcc_hist(pcc_list,
             bin_num=18, bin_color='#696969', bin_alpha=0.75,
             median_line=True, median_color='#009ACD', median_width=3,
             percent_list=(90, 80, 70),
             label_fontsize=8,
             anno_fontsize=8, anno_y_site=(0.75, 0.5, 0.4),
             ax=None, save=None):
    if ax is None:
        ax = plt.gca()

    median_pcc = np.median(pcc_list)
    pcc_num = len(pcc_list)

    ax.set_xlim(0, 1)
    ax.set_xticks(np.linspace(0, 1, 6))
    set_thousand_separate(ax)

    hist = ax.hist(pcc_list, bins=bin_num, alpha=bin_alpha, color=bin_color, edgecolor='k')

    if median_line:
        mid_line = ax.axvline(median_pcc, linewidth=median_width, color=median_color)
    else:
        mid_line = None

    ax.set_xlabel("PCC", fontsize=label_fontsize)
    ax.set_ylabel("Number of test peptide precursors", fontsize=label_fontsize)

    percent_list = sorted(map(lambda x: x/100, percent_list))
    pcc_percent_list = []
    anno_title = '>PCC Percentage'
    pcc_anno_list = [anno_title]
    for pcc in percent_list:
        ratio = np.sum(pcc_list > pcc) / pcc_num
        pcc_percent_list.append(ratio)
        pcc_anno_list.append(f'>{pcc:.2f}  {ratio:.1%}')

    ax.annotate('\n'.join(pcc_anno_list), xy=(0.05, ax.get_ylim()[1] * anno_y_site[0]), fontsize=anno_fontsize)
    ax.annotate('Median PCC: {:.2f}'.format(median_pcc), xy=(0.05, ax.get_ylim()[1] * anno_y_site[1]), fontsize=anno_fontsize)
    ax.annotate(r'n = {:,}'.format(pcc_num), xy=(0.05, ax.get_ylim()[1] * anno_y_site[2]), fontsize=anno_fontsize)

    if save:
        plt.savefig(save + '.PCC.png')

    return hist, mid_line, pcc_anno_list