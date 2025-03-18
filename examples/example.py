from orbitals import OrbitalMotion

o = OrbitalMotion(G=1.0, M=1.0)

t, state = 0, [1, 0, 0, 0.5]  # t, x, y, vx, vy

print(o(t, state))
