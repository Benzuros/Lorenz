import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lorenz import Lorenz



def animation1():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.view_init(15, -60, 0)

    l1 = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l1.simulate((1, 1, 1))
    l1.simulate((1, 1, 1.01))
    l1.simulate((1, 1.01, 1))
    l1.simulate((1.01, 1, 1))
    ani = l1.animate_trajectories(fig, ax, 5)
    plt.show()



if __name__ == '__main__':
    animation1()