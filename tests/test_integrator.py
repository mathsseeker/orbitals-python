from orbitals import EulerIntegrator


def test_euler():
    # Check Euler by integrating f=5*x
    factor = 5.0
    initial = 1.0
    dt = 0.01

    eq = lambda t, state: [factor * state[0]]
    i = EulerIntegrator(eq, dt=dt)
    t, state = 0, [initial]
    assert i.step(t, state) == (dt, [initial + factor * initial * dt])
