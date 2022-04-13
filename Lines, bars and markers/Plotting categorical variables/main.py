import matplotlib.pyplot as plt
import numpy as np


def main():
    data = dict(apple=10, orange=15, lemon=5, lime=20)
    names = list(data.keys())
    values = list(data.values())

    fig, ax = plt.subplots(1, 3, figsize=(9, 3), sharey=True)  # share_y
    ax[0].bar(names, values)
    ax[1].scatter(names, values)
    ax[2].plot(names, values)
    fig.suptitle('Categorical Plotting')
    plt.savefig('main.png')
    plt.close(fig)

    b = 'bored'
    h = 'happy'
    cat = [b, h, b, b, h, b]
    dog = [h, h, h, h, b, b]
    activity = ['combing', 'drinking', 'feeding', 'napping', 'playing', 'washing']

    fig, ax = plt.subplots()
    ax.plot(activity, dog, label='dog')
    ax.plot(activity, cat, label='cat')
    ax.invert_yaxis()
    ax.legend()
    plt.savefig('main2.png')
    return


if __name__ == '__main__':
    main()
