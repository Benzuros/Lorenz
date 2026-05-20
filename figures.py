import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lorenz import Lorenz



def figure1():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')

    l1 = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l1.simulate((1, 1, 1))
    l1.simulate((1, 1, 1.01))
    l1.simulate((1, 1.01, 1))
    l1.simulate((1.01, 1, 1))
    l1.plot_trajectories(ax)

    ax.legend()
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax.view_init(0, -90, 0)
    plt.show()



if __name__ == '__main__':
    figure1()