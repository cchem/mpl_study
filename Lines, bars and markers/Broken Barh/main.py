import matplotlib.pyplot as plt
import numpy as np

bill_start = [110, 150]
bill_duration = [30, 10]
bill_x = [(i, j) for i, j in zip(bill_start, bill_duration)]
bill_y_bottom = 10
bill_y_height = 9
bill_y = (bill_y_bottom, bill_y_height)

jim_start = [10, 100, 130]
jim_duration = [50, 20, 10]
jim_x = [(i, j) for i, j in zip(jim_start, jim_duration)]
jim_y_bottom = 20
jim_y_height = 9
jim_y = (jim_y_bottom, jim_y_height)


def main():
    fig, ax = plt.subplots()
    ax.broken_barh(bill_x, bill_y, facecolors='tab:blue')
    ax.broken_barh(jim_x, jim_y, facecolors=('tab:orange', 'tab:green', 'tab:red'))

    ax.set_ylim(5, 35)
    ax.set_xlim(0, 200)
    ax.set_xlabel('seconds since start')
    ax.set_yticks([15, 25], labels=['Bill', 'Jim'])
    ax.grid(True)

    annotation_text = 'race interrupted'
    arrowhead_coord = (61, 25)
    arrow_settings = dict(facecolor='black', shrink=0.05)
    text_position_settings = dict(
        fontsize=16, xytext=(0.8, 0.9), textcoords='axes fraction',
        horizontalalignment='right', verticalalignment='top')

    ax.annotate(annotation_text, arrowhead_coord,
                arrowprops=arrow_settings, **text_position_settings)
    plt.savefig('main.png')
    return


if __name__ == '__main__':
    main()
