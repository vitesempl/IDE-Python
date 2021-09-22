# RK-IDE-Python
Package for solving Differential equations with Discrete and Distributed delays by the explicit Runge-Kutta method.

# Tools and packages

* Python 3.9 (VERSION ≥ v"3.6")
* numpy
* matplotlib
* Jupyter Notebook / Google Colaboratory

# Usage

```
from RK.ide import ide_solve
```

```
sol = ide_solve(idefun, K, delays_int, history, tspan, stepsize, delays=delays, overlapping=True)
```

|  #  | Argument    | Description |
| --- | :---        |    :---     |
|  1  | idefun      | right-hand side function (*t* - time, *y* - solution, *z* - discrete delays, *i* - integrals) |
|  2  | K           | Kernel (integrated function) |
|  3  | delays_int  | distributed delays function (lower integration limit) |
|  4  | history     | history function |
|  5  | tspan       | solution interval |
|  6  | stepsize    | step of numerical Runge-Kutta method |
|  7  | delays      | (optional) discrete delays function (if idefun has 'z') |
|  8  | overlapping | (optional) if equation has overlapping in discrete delays. This option uses the 7-step method |

Examples of use can be found in the Notebook and in scripts from the folder `/Scripts`.

# Authors

* Aleksandr Lobaskin (Saint Petersburg State University)
* Alexey Eremin (Saint Petersburg State University)

# Special thanks

* Yukihiko Nakata (Shimane University) (examples from SIR-models)

# License

"RK-IDE-Julia" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).