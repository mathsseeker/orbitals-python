from abc import ABC, abstractmethod
import numpy as np


class DifferentialEquation(ABC):
    @abstractmethod
    def __call__(self, t, state):
        pass


class OrbitalMotion(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M

    def __call__(self, t, state):
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        ax = -self.G * self.M * x / r**3
        ay = -self.G * self.M * y / r**3
        return [vx, vy, ax, ay]


class OrbitalMotionTwoSuns(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M

    def __call__(self, t, state):
        x, y, vx, vy = state
        r = np.sqrt(x**2 + y**2)
        # Second sun at (2,0)
        rp = np.sqrt((x - 2) ** 2 + y**2)
        ax = -self.G * self.M * x / r**3 - self.G * self.M * (x - 2) / rp**3
        ay = -self.G * self.M * y / r**3 - self.G * self.M * y / rp**3
        return [vx, vy, ax, ay]
