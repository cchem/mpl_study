import matplotlib.pyplot as plt
import numpy as np
from matplotlib._enums import CapStyle


def main():
    CapStyle.demo()
    plt.savefig('main.png')
    return


if __name__ == '__main__':
    main()
