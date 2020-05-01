from bioplotkit.colors.precolors_single import S

from matplotlib import pyplot as plt
from scipy.stats import pearsonr
from mskit.stats import calc_delta_tx, calc_r_square


def define_reg_ax(ax, rt_1, rt_2, expand=0.2):
    rt_range = (min(min(rt_1), min(rt_2)), max(max(rt_1), max(rt_2)))
    rt_width = rt_range[1] - rt_range[0]
    min_axis = rt_range[0] - rt_width * expand
    max_axis = rt_range[1] + rt_width * expand
    ax.set_xlim(min_axis, max_axis)
    ax.set_ylim(min_axis, max_axis)
    ax.set_aspect('equal')
    ax.set_xlabel('Observerd RT')
    ax.set_ylabel('Predicted RT')
    return min_axis, max_axis


def ex_line_dict(obse_rt, pred_rt, ex_line):
    ex_dict = dict()
    ex_line = sorted(list(ex_line), reverse=True)
    for _each_ex in ex_line:
        _each_ex = _each_ex * 100 if _each_ex <= 1 else _each_ex
        ex_dict[str(_each_ex)] = calc_delta_tx(obse_rt, pred_rt, _each_ex / 100)
    return ex_dict


def rt_reg(obse_rt, pred_rt, ex_line=(95, ), ax=None, diagonal=True, linewidth=1., anno_fontsize=10, anno_gap=12.5, title=None, save=None):
    if ax is None:
        ax = plt.gca()
    min_axis, max_axis = define_reg_ax(ax, obse_rt, pred_rt)

    p = pearsonr(obse_rt, pred_rt)
    r_square = calc_r_square(obse_rt, pred_rt)

    annotate_text = [f'PCC: {p[0]:.4f}',
                     f'R$^2$: {r_square:.4f}']

    if ex_line:
        ex_dict = ex_line_dict(obse_rt, pred_rt, ex_line)
    else:
        ex_dict = None

    title = title if title else 'RT correlation'
    ax.set_title(title)

    scat = ax.scatter(obse_rt, pred_rt, c='b', s=1.5)

    if diagonal:
        ax.plot([min_axis, max_axis], [min_axis, max_axis], color='k', linewidth=linewidth)
    if ex_dict:
        for _i, (_ex_num, _ex_value) in enumerate(ex_dict.items()):
            try:
                _color = S[_i]
            except IndexError:
                _color = 'k'
            plt.plot([min_axis, max_axis], [min_axis - _ex_value / 2, max_axis - _ex_value / 2], color=_color, linewidth=linewidth)
            plt.plot([min_axis, max_axis], [min_axis + _ex_value / 2, max_axis + _ex_value / 2], color=_color, linewidth=linewidth)
            annotate_text.append(rf'$\Delta$t{_ex_num}: {_ex_value:.3f}')

    annotate_text.append(f'n={len(obse_rt)}')
    annotation = []
    for _i, _anno in enumerate(annotate_text):
        _ = ax.annotate(_anno, xy=(min_axis, max_axis), fontsize=anno_fontsize,
                        va='top', ha='left',
                        textcoords='offset points', xytext=(5, -anno_gap * (_i + 0.5)))
        annotation.append(_)

    if save:
        plt.savefig(save + '.RT.png')

    return scat, annotation
