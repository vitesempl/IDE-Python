from RK.ide import ide_solve

from math import *
import numpy as np

import time

def OutputSolution():
    nz = np.size(history(tspan[0]))
    if nz == 1:
        print("y(", tspan[1], ") = ", sol[1][-1], sep='')
    else:
        for i in range(nz):
            print("y", i + 1, "(", tspan[1], ") = ", sol[1][i, -1], sep='')


# Test 2
tspan = [0, 5]
stepsize = 1e-2
def idefun(t, y, z, i): return - y**2 - t * exp(t**2) * z**4 * i
def         K(t, s, y): return [y * exp(s - s * t)]
def        delays(t,y): return [t / 2]
def      delays_int(t): return [t - 1]
def         history(t): return exp(-t)

t = time.time()
sol = ide_solve(idefun, K, delays_int, history, tspan, stepsize, delays=delays, overlapping=True)
elapsed = time.time() - t

OutputSolution()
print("Elapsed time:", elapsed, "seconds")

# Test 3
tspan = [0, 5]
stepsize = 1e-2
def idefun(t, y, z, i): return exp(1) - exp(t**2) / z**2 * (i[0] - exp(-2 * t) * i[1]) * (t - 1)
def         K(t, s, y): return [y * exp(-s * t),
                                y * exp(t * (2 - s))]
def       delays(t, y): return [t - 1]
def      delays_int(t): return [t - 1,
                                t - 2]
def         history(t): return exp(t)

t = time.time()
sol = ide_solve(idefun, K, delays_int, history, tspan, stepsize, delays=delays, overlapping=True)
elapsed = time.time() - t

OutputSolution()
print("Elapsed time:", elapsed, "seconds")

# Test 4
tspan = [0, 5]
stepsize = 1e-2
def idefun(t, y, z, i): return - z[0, 0]**((t + 1) / 2) * z[0, 1] * y**2 * (1 + exp(t**2) * t * i) / exp(1 / 2)
def         K(t, s, y): return [y * exp(s - s * t)]
def       delays(t, y): return [log(y)**2 / (t + 1) - 1 / 2,
                                (t - 1) / 4]
def      delays_int(t): return [t / 2 - 1]
def         history(t): return exp(-t)

t = time.time()
sol = ide_solve(idefun, K, delays_int, history, tspan, stepsize, delays=delays, overlapping=True)
elapsed = time.time() - t

OutputSolution()
print("Elapsed time:", elapsed, "seconds")