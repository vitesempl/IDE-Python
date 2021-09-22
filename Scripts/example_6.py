from RK.ide import ide_solve

from math import *
import numpy as np
import matplotlib.pyplot as plt


def OutputSolution():
    nz = np.size(history(tspan[0]))
    if nz == 1:
        print("y(", tspan[1], ") = ", sol[1][-1], sep='')
    else:
        for i in range(nz):
            print("y", i + 1, "(", tspan[1], ") = ", sol[1][i, -1], sep='')


def OutputPlot():
    nz = np.size(history(tspan[0]))
    fig = plt.figure(figsize=[9, 5])
    if nz == 1:
        fig = plt.plot(sol[0], sol[1], label="y(t)")
    else:
        for i in range(nz):
            fig = plt.plot(sol[0], sol[1][i], label="y" + str(i + 1) + "(t)")
    plt.title("NUMERICAL SOLUTION")
    plt.legend(fontsize=14)
    plt.xlabel("TIME", fontsize=14)
    plt.ylabel("SOLUTION", fontsize=14)
    plt.grid()


# Example 6 (system of equations)
tspan = [0, 10]
stepsize = 1e-2
def idefun(t, y, z, i): return [-2.5 * i[0],
                                -15 * i[1],
                                0.001 * exp(t)]
def         K(t, s, y): return [sin(y[0]),
                                sin(y[1])]
def      delays_int(t): return [t - 1,
                                t - 1]
def         history(t): return [1.5,
                                1.5,
                                0.001 * exp(t)]

sol = ide_solve(idefun, K, delays_int, history, tspan, stepsize)
OutputSolution()
OutputPlot()

plt.show()
