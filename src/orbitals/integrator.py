from abc import ABC, abstractmethod


class Integrator(ABC):
    def __init__(self, equation, dt):
        self.equation = equation
        self.dt = dt

    @abstractmethod
    def step(self, t, state):
        pass


class EulerIntegrator(Integrator):
    def step(self, t, state):
        derivatives = self.equation(t, state)
        new_state = [s + ds * self.dt for s, ds in zip(state, derivatives)]
        return t + self.dt, new_state


class RK4Integrator(Integrator):
    def step(self, t, state):
        f = self.equation
        dt = self.dt
        k1 = f(t, state)
        k2 = f(t + dt / 2, [s + k1_i * dt / 2 for s, k1_i in zip(state, k1)])
        k3 = f(t + dt / 2, [s + k2_i * dt / 2 for s, k2_i in zip(state, k2)])
        k4 = f(t + dt, [s + k3_i * dt for s, k3_i in zip(state, k3)])
        new_state = [
            s + (dt / 6) * (k1_i + 2 * k2_i + 2 * k3_i + k4_i)
            for s, k1_i, k2_i, k3_i, k4_i in zip(state, k1, k2, k3, k4)
        ]
        return t + dt, new_state
