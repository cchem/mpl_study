import matplotlib.pyplot as plt
import numpy as np

from matplotlib.path import Path
from matplotlib.patches import PathPatch


def main():
    n = 400
    t = np.linspace(0, 2 * np.pi, n)
    r = 0.5 + np.cos(t)
    x, y = r * np.cos(t), r * np.sin(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'k')
    ax.set(aspect=1)
    plt.savefig('main.png')
    return


def main2():
    n = 400
    t = np.linspace(0, 2 * np.pi, n)
    r = 0.5 + np.cos(t)
    x, y = r * np.cos(t), r * np.sin(t)

    axs = (plt.figure(constrained_layout=True).subplots(1, 2, sharex=True, sharey=True))
    errs = [
        (axs[0], 'constant error', 0.05),
        (axs[1], 'variable error', 0.05 * np.sin(2 * t) ** 2 + 0.04),
    ]

    for i, (ax, title, err) in enumerate(errs):
        ax.set(title=title, aspect=1, xticks=[], yticks=[])
        ax.plot(x, y, 'k')
        draw_error_bar(ax, x, y, err=err,
                       facecolor=f'C{i}', edgecolor='none', alpha=.3)
    plt.savefig('main2.png')


def draw_error_bar(ax, x, y, err, **kwargs):
    dx = np.concatenate([[x[1] - x[0]], x[2:] - x[:-2], [x[-1] - x[-2]]])
    dy = np.concatenate([[y[1] - y[0]], y[2:] - y[:-2], [y[-1] - y[-2]]])
    l = np.hypot(dx, dy)  # dx, dyで貼られる直角三角形の斜辺の長さ
    nx = dy / l
    ny = -dx / l

    xp = x + nx * err
    xn = x - nx * err
    yp = y + ny * err
    yn = y - ny * err

    vertices = np.block([[xp, xn[::-1]],
                         [yp, yn[::-1]]]).T
    codes = np.full(len(vertices), Path.LINETO)
    codes[0] = codes[len(xp)] = Path.MOVETO
    path = Path(vertices, codes)
    ax.add_patch(PathPatch(path, **kwargs))


if __name__ == '__main__':
    main()
    main2()
