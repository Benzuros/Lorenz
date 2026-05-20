import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



class Lorenz:
    def __init__(self, sigma, r, b, t, h):
        self.sigma = sigma
        self.r = r
        self.b = b
        self.t = t
        self.h = h
        t += h
        self.ts = np.arange(0, t, h)

        def f(u):
            x, y, z = u
            xx = sigma * (y - x)
            yy = x * (r - z) - y
            zz = x * y - b * z
            return np.array([xx, yy, zz])

        self.f = f
        self.trajectories = {}


    def simulate(self, u0):
        """Simulate *u\'(t) = f(u), u(0) = u0* using RK4 numerical scheme
            in the time interval [0 ; t] with step h."""
        u0 = tuple(float(i) for i in u0)
        us = np.array([u0 for _ in self.ts])

        for i in range(len(self.ts) - 1):
            k1 = self.f(us[i])
            k2 = self.f(us[i] + self.h / 2 * k1)
            k3 = self.f(us[i] + self.h / 2 * k2)
            k4 = self.f(us[i] + self.h * k3)
            us[i + 1] = us[i] + self.h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

        self.trajectories[u0] = us.T
        return us.T


    def plot_values(self, ax, which):
        if which == "x":
            which = 0
        elif which == "y":
            which = 1
        elif which == "z":
            which = 2

        for u0 in self.trajectories:
            x0, y0, z0 = u0
            vs = self.trajectories[u0][which]
            ax.plot(self.ts, vs, lw=0.5, label=f"$u_0 = {x0}, {y0}, {z0}$")


    def plot_trajectories(self, ax):
        for u0 in self.trajectories:
            x0, y0, z0 = u0
            xs, ys, zs = self.trajectories[u0]
            ax.plot(xs, ys, zs, lw=0.5, label=f"$u_0 = {x0}, {y0}, {z0}$")

    def animate_trajectories(self, fig, ax, speed, *, legend:bool=True):
        lines = {}
        for u0 in self.trajectories:
            #initialize lines
            x0, y0, z0 = u0
            xs, ys, zs = self.trajectories[u0]
            lines[u0] = ax.plot(xs[0], ys[0], zs[0], lw=0.5, label=f"$u_0 = {x0}, {y0}, {z0}$")[0]

        if legend:
            ax.legend()

        def update(frame):
            for u0, line in lines.items():
                xs, ys, zs = self.trajectories[u0]
                line.set_xdata(xs[:frame*speed:speed])
                line.set_ydata(ys[:frame*speed:speed])
                line.set_3d_properties(zs[:frame*speed:speed])
            return tuple(lines.values())

        ani = FuncAnimation(fig, update, frames=len(self.ts)//speed, interval=1, repeat=False)

        return ani


if __name__ == '__main__':
    l = Lorenz(10, 28, 8/3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1, 1, 1.01))

    Fig = plt.figure(figsize=(10, 5))
    ax0 = Fig.add_subplot(121, projection='3d', xlabel="$x$", ylabel="$y$", zlabel="$z$",
                          xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))
    ax0.view_init(15, -60, 0)
    ax1 = Fig.add_subplot(322, xlim=(0, 100), title="$x$")
    ax2 = Fig.add_subplot(324, sharex=ax1, title="$y$")
    ax3 = Fig.add_subplot(326, sharex=ax1, title="$z$")
    Fig.subplots_adjust(hspace=0.4, wspace=0.3)

    l.plot_trajectories(ax0)
    l.plot_values(ax1, 0)
    l.plot_values(ax2, 1)
    l.plot_values(ax3, 2)

    ax0.legend()

    plt.show()
