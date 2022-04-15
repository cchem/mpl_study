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
    plt.show()
    return





if __name__ == '__main__':
    main()
