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


    def plot_trajectories(self, ax):
        for u0 in self.trajectories:
            x0, y0, z0 = u0
            xs, ys, zs = self.trajectories[u0]
            ax.plot(xs, ys, zs, lw=0.5, label=f"$u_0 = {x0}, {y0}, {z0}$")

    def animate_trajectories(self, fig, ax, speed):
        lines = {}
        for u0 in self.trajectories:
            #initialize lines
            x0, y0, z0 = u0
            xs, ys, zs = self.trajectories[u0]
            lines[u0] = ax.plot(xs[0], ys[0], zs[0], lw=0.5, label=f"$u_0 = {x0}, {y0}, {z0}$")[0]

        ax.legend()
        ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$", xlim=(-20, 20), ylim=(-30, 30), zlim=(0, 50))

        def update(frame):
            for u0, line in lines.items():
                xs, ys, zs = self.trajectories[u0]
                line.set_xdata(xs[:frame*speed:speed])
                line.set_ydata(ys[:frame*speed:speed])
                line.set_3d_properties(zs[:frame*speed:speed])
            return tuple(lines.values())

        ani = FuncAnimation(fig, update, frames=len(self.ts)//speed, interval=1, repeat=False, blit=True)

        return ani


if __name__ == '__main__':
    Fig = plt.figure(figsize=(5, 5))
    Ax = Fig.add_subplot(projection='3d')

    l = Lorenz(10, 28, 8 / 3, 100, 0.001)
    l.simulate((1, 1, 1))
    l.simulate((1.01, 1, 1))
    # l.simulate((11, -4, 10))
    # l.simulate((-7, -6, 17))
    # l.simulate((-5, 5, -14))
    #l.plot_trajectories(Ax)
    #
    # Ax.legend()
    # Ax.set(xlabel="$x$", ylabel="$y$", zlabel="$z$")
    Ani = l.animate_trajectories(Fig, Ax, 5)
    plt.show()
