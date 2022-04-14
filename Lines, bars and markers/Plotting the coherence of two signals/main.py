import matplotlib.pyplot as plt
import numpy as np


def main():
    np.random.seed(19680801)

    dt = 0.01
    t = np.arange(0, 30, dt)
    nse1 = np.random.randn(len(t))
    nse2 = np.random.randn(len(t))

    s1 = np.sin(2 * np.pi * 10 * t) + nse1
    s2 = np.sin(2 * np.pi * 10 * t) + nse2

    fig, ax = plt.subplots(2, 1)
    ax[0].plot(t, s1, t, s2)
    ax[0].set_xlim(0, 2)
    ax[0].set_xlabel('time')
    ax[0].set_ylabel('s1, and s2')
    ax[0].grid(True)

    cxy, f = ax[1].cohere(s1, s2, 256, 1 / dt)
    ax[1].set_ylabel('coherence')
    fig.tight_layout()
    plt.savefig('main.png')
    return


if __name__ == '__main__':
    main()
