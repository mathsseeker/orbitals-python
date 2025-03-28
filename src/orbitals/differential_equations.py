from abc import ABC, abstractmethod
import numpy as np


class DifferentialEquation(ABC):
    @abstractmethod
    def __call__(self, t, state):#this only gives information about how the method should be
        pass


class OrbitalMotion(DifferentialEquation):
    def __init__(self, G, M):
        self.G = G
        self.M = M

    def __call__(self, t, state):
        x, y, vx, vy = state
        
        r = np.sqrt(x**2 + y**2)
        if r == 0:
            print("Imposible for the planet to be in the same place as the star")
        else:
         ax = -self.G * self.M * x / r**3
         ay = -self.G * self.M * y / r**3
         return [vx, vy, ax, ay]


class OrbitalMotionTwoSuns(DifferentialEquation):
    """
    Represents the orbital motion of a body influenced by the gravitational forces 
    of two suns. This class defines a system of differential equations to compute 
    the acceleration and velocity of the body at any given time.
    Attributes:
        G (float): Gravitational constant.
        M (float): Mass of each sun (assumed to be equal for both suns).
    Methods:
        __call__(t, state):
            Computes the derivatives of the state variables (position and velocity) 
            at a given time.
    Parameters:
        t (float): The current time (not explicitly used in the computation, 
                   but required for compatibility with numerical solvers).
        state (list or array-like): The current state of the system, represented 
                                    as [x, y, vx, vy], where:
                                    - x, y are the position coordinates of the body.
                                    - vx, vy are the velocity components of the body.
    Returns:
        list: A list containing the derivatives [vx, vy, ax, ay], where:
              - vx, vy are the velocity components (unchanged from the input state).
              - ax, ay are the acceleration components computed based on the 
                gravitational forces exerted by the two suns.
    Notes:
        - The first sun is assumed to be located at the origin (0, 0).
        - The second sun is assumed to be located at (2, 0).
        - The gravitational force is computed using Newton's law of gravitation, 
          and the acceleration is derived accordingly.
    """
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
