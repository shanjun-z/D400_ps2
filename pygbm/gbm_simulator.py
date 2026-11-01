# D400 (C1) Problem Set 2, Exercise 2
# install the relevant packages
import numpy as np
import matplotlib.pyplot as plt

class GBMSimulator:
    """Differential equation: Y(t) = y0 * exp((mu - sigma^2/2) t + sigma B(t))."""
    def __init__(self, y0, mu, sigma):
        self.y0 = y0
        self.mu = mu
        self.sigma = sigma

    def simulate(self, T, N, dt=1.0, seed=None):
        """
        Simulate N independent paths over T times steps with time increment dt.
        Returns (t, Y) where t is the time vector and Y is a matrix of shape (N, T+1) containing the simulated paths.
        """
        rng = np.random.default_rng(seed)
        t = np.arange(T + 1) * dt

        # specify a distribution of the Brownian motion increments
        # Brownian increments dB ~ N(0, dt), cumulated to get B(t), B(0) = 0
        dB = rng.normal(0.0, np.sqrt(dt), size=(N, T))
        B = np.concatenate([np.zeros((N, 1)), np.cumsum(dB, axis=1)], axis=1)

        # Compute the exact solution of the geometric Brownian motion
        Y = self.y0 * np.exp((self.mu - 0.5 * self.sigma**2) * t + self.sigma * B)
        return t, Y

    def plot(self, T, N, dt=1.0, seed=None):
        """
        Plot N independent paths of the geometric Brownian motion over T time steps with time increment dt.
        """
        t, Y = self.simulate(T, N, dt, seed)
        plt.plot(t, Y.T, lw=0.8)
        plt.xlabel("Time")
        plt.ylabel("Y(t)")
        plt.title(f"Simulated Geometric Brownian Motion Path: mu={self.mu}, sigma={self.sigma}, y0={self.y0}, {N} paths")
        plt.legend()
        plt.show()