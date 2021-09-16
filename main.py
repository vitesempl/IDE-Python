from RK.ide import ide_solve, ide_delay_solve

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


def OutputConvOrder(dde=True):
    nz = np.size(history(tspan[0]))

    plt.rcParams['figure.figsize'] = [10, 5]
    fig, axs = plt.subplots(1, 2)

    if nz == 1:
        axs[0].plot(sol[0], sol[1], label="y(t)")
    else:
        for i in range(nz):
            axs[0].plot(sol[0], sol[1][i], label="y" + str(i + 1) + "(t)")
    axs[0].grid()
    axs[0].set_title("NUMERICAL SOLUTION")
    axs[0].legend(loc='upper left', fontsize=12)
    axs[0].set_xlabel("TIME", fontsize=14)
    axs[0].set_ylabel("SOLUTION", fontsize=14)

    nb = 1
    n = 7
    err = []
    nsteps = []

    for steppow in range(nb, n):
        stepsize = 2**(-steppow)
        if dde:
            sol_test = ide_delay_solve(idefun, K, delays_int, history, tspan, stepsize, delays=delays)
        else:
            sol_test = ide_delay_solve(idefun, K, delays_int, history, tspan, stepsize)
        err.append(abs(analytic_sol - sol_test[1][-1]))
        nsteps.append(stepsize)

    print("Convergence order:", (log10(err[-1]) - log10(err[-2])) / (log10(pow(2, -n)) - log10(pow(2, -n + 1))))

    axs[1].plot(nsteps, err)
    axs[1].grid()

    axs[1].set_title("CONVERGENCE ORDER")
    axs[1].set_xscale('log')
    axs[1].set_yscale('log')
    axs[1].set_xlabel("STEPSIZE", fontsize=14)
    axs[1].set_ylabel("ERROR", fontsize=14)

    fig.tight_layout()


# Example 1 (only integral)
tspan = [1.1, 5]
def idefun(t, y, z, i): return ((t - 1) * exp(t ** 2) * i) / (exp(-1) * y - 1)
def      K(t, s, y): return [y * exp(-s * t)]
def   delays_int(t): return [t - 1]  # delays of integrals
def      history(t): return exp(t)

def fun(t): return exp(t)
analytic_sol = fun(tspan[1])

sol = ide_delay_solve(idefun, K, delays_int, history, tspan, 1e-2)
OutputSolution()
OutputPlot()
OutputConvOrder(dde=False)

# Example 2 (integral+discrete delays)
tspan = [0, 10]
def idefun(t, y, z, i): return (1 + exp(-pi / 2)) * y - exp(-pi / 2) * z - 2 * exp(-2 * t) * i
def         K(t, s, y): return [y * exp(t + s)]
def       delays(t, y): return [t - pi / 2]  # delays of z
def      delays_int(t): return [t - pi / 2]
def         history(t): return cos(t)

def fun(t): return cos(t)
analytic_sol = fun(tspan[1])

sol = ide_delay_solve(idefun, K, delays_int, history, tspan, 1e-2, delays=delays)
OutputSolution()
OutputPlot()
OutputConvOrder(dde=True)

plt.show()
