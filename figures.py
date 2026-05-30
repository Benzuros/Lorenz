import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from lorenz import Lorenz



def figure1():
    l = Lorenz(28, 10, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))
    l.simulate((1, 1.01, 1))
    l.simulate((1.01, 1, 1))

    fig = plt.figure(figsize=(10, 10))
    fig.tight_layout()

    ax = fig.add_subplot(projection='3d', xlabel="$x$", ylabel="$y$", zlabel="$z$",
                         xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax.set(title=r"$r = 28$, $\sigma = 10$, $b = \frac{8}{3}$")
    ax.view_init(15, -60, 0)

    l.plot_trajectories(ax)
    ax.legend()


def figure2():
    l = Lorenz(28, 10, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))
    l.simulate((1, 1.01, 1))
    l.simulate((1.01, 1, 1))

    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10, 3.5))
    fig.tight_layout(rect=[0.02, 0.05, 1, 0.95])

    ax1.set(xlim=(-20, 20), ylim=(-30, 30), xlabel="$x$", ylabel="$y$")
    l.plot_trajectories2d(ax1, ("x", "y"))
    fig.legend(loc="upper left", framealpha=1)

    ax2.set(xlim=(-20, 20), ylim=(0, 50), xlabel="$x$", ylabel="$z$")
    l.plot_trajectories2d(ax2, ("x", "z"))

    ax3.set(xlim=(-30, 30), ylim=(0, 50), xlabel="$y$", ylabel="$z$")
    l.plot_trajectories2d(ax3, ("y", "z"))

    fig.subplots_adjust(wspace=0.3, hspace=0.3)

    fig.suptitle(r"$r = 28$, $\sigma = 10$, $b = \frac{8}{3}$")


def figure3():
    l = Lorenz(28, 10, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))

    fig = plt.figure(figsize=(10, 5))
    fig.tight_layout()
    ax0 = fig.add_subplot(121, projection='3d', xlabel="$x$", ylabel="$y$", zlabel="$z$",
                          xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax0.set(title=r"$r = 28$, $\sigma = 10$, $b = \frac{8}{3}$")
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


def figure4():
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(projection='3d')
    ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-15, 15), ylim=(-15, 15), zlim=(0, 30))
    ax.set(title=r"$r = 0.5$, $\sigma = 10$, $b = \frac{8}{3}$")
    fig.tight_layout()
    ax.view_init(20, -50, 0)

    l = Lorenz(0.5, 10, 8 / 3, 10, 0.001)
    for x in -15, 0, 15:
        for y in -15, 0, 15:
            for z in 0, 10, 20, 30:
                l.simulate((x, y, z))
    l.plot_trajectories(ax)


def figure5():
    fig = plt.figure(figsize=(10, 10))
    ax1 = fig.add_subplot(221, projection='3d')
    ax2 = fig.add_subplot(222, projection='3d')
    ax3 = fig.add_subplot(223, projection='3d')
    ax4 = fig.add_subplot(224, projection='3d')
    ax1.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-15, 15), ylim=(-15, 15), zlim=(0, 30))
    ax1.set(title=r"$r = 5$, $\sigma = 10$, $b = \frac{8}{3}$")
    ax1.view_init(15, -50, 0)
    ax2.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-15, 15), ylim=(-15, 15), zlim=(0, 30))
    ax2.set(title=r"$r = 10$, $\sigma = 10$, $b = \frac{8}{3}$")
    ax2.view_init(15, -50, 0)
    ax3.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax3.set(title=r"$r = 20$, $\sigma = 10$, $b = \frac{8}{3}$")
    ax3.view_init(15, -50, 0)
    ax4.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax4.set(title=r"$r = 28$, $\sigma = 10$, $b = \frac{8}{3}$")
    ax4.view_init(15, -50, 0)


    l1 = Lorenz(5, 10, 8 / 3, 10, 0.001)
    l2 = Lorenz(10, 10, 8 / 3, 10, 0.001)
    l3 = Lorenz(20, 10, 8 / 3, 10, 0.001)
    l4 = Lorenz(28, 10, 8 / 3, 10, 0.001)

    for l in l1, l2, l3, l4:
        for x in -15, 0, 15:
            for y in -15, 0, 15:
                for z in 0, 10, 20, 30:
                    l.simulate((x, y, z))
    l1.plot_trajectories(ax1)
    l2.plot_trajectories(ax2)
    l3.plot_trajectories(ax3)
    l4.plot_trajectories(ax4)


if __name__ == '__main__':
    figure5()
    plt.show()