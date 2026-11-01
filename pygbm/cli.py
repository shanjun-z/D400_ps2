import argparse
import numpy as np
import matplotlib.pyplot as plt
from .gbm_simulator import GBMSimulator


def main(argv=None):
    p = argparse.ArgumentParser(prog="pygbm", description="Simulate geometric Brownian motion.")
    p.add_argument("--y0", type=float, default=1.0, help="initial value (default 1.0)")
    p.add_argument("--mu", type=float, required=True, help="drift")
    p.add_argument("--sigma", type=float, required=True, help="diffusion coefficient")
    p.add_argument("-T", type=int, default=252, help="number of time steps (default 252)")
    p.add_argument("-N", type=int, default=10, help="number of simulated paths (default 10)")
    p.add_argument("--dt", type=float, default=1.0, help="time increment (default 1.0)")
    p.add_argument("--seed", type=int, default=None, help="random seed")
    p.add_argument("--plot", action="store_true", help="show a plot of the paths")
    a = p.parse_args(argv)

    sim = GBMSimulator(a.y0, a.mu, a.sigma)
    t, Y = sim.simulate(a.T, a.N, a.dt, a.seed)

    final = Y[:, -1]
    print(f"Simulated {a.N} path(s) over {a.T} steps (dt={a.dt:g})")

    if a.plot or a.save_plot:
        plt.plot(t, Y.T, lw=0.8)
        plt.xlabel("Time")
        plt.ylabel("Y(t)")
        plt.title(f"Simulated GBM: mu={a.mu}, sigma={a.sigma}, y0={a.y0}, {a.N} paths")
        if a.plot:
            plt.show()


if __name__ == "__main__":
    main()