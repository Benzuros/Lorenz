import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lorenz import Lorenz


def animation1():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-20, 20), zlim=(0, 50))
    ax.view_init(15, -60, 0)

    l = Lorenz(10, 10, 8 / 3, 10, 0.001)
    for x in -10, 0, 10:
        for y in -10, 0, 10:
            for z in 0, 10, 20, 30, 40:
                l.simulate((x, y, z))
    ani = l.animate_trajectories(fig, ax, 5, legend=False)
    plt.show()


def animation2():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax.view_init(15, -60, 0)

    l = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))
    l.simulate((1, 1.01, 1))
    l.simulate((1.01, 1, 1))
    ani = l.animate_trajectories(fig, ax, 5)
    plt.show()



if __name__ == '__main__':
    animation1()