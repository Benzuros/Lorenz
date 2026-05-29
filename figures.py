import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lorenz import Lorenz



def figure1():
    l = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))
    l.simulate((1, 1.01, 1))
    l.simulate((1.01, 1, 1))

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d', xlabel="$x$", ylabel="$y$", zlabel="$z$",
                         xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax.view_init(15, -60, 0)

    l.plot_trajectories(ax)
    ax.legend()
    plt.show()


def figure2():
    l = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))

    fig = plt.figure(figsize=(10, 5))
    fig.tight_layout()
    ax0 = fig.add_subplot(121, projection='3d', xlabel="$x$", ylabel="$y$", zlabel="$z$",
                          xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax0.view_init(15, -60, 0)
    ax1 = fig.add_subplot(322, xlim=(0, 100), title="$x$")
    ax2 = fig.add_subplot(324, sharex=ax1, title="$y$")
    ax3 = fig.add_subplot(326, sharex=ax1, title="$z$")
    fig.subplots_adjust(hspace=0.4, wspace=0.3)

    l.plot_trajectories(ax0)
    l.plot_values(ax1, 0)
    l.plot_values(ax2, 1)
    l.plot_values(ax3, 2)
    ax0.legend()
    plt.show()


if __name__ == '__main__':
    figure2()