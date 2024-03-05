import numpy
import matplotlib.pyplot as plot


def dichotomy_find_min(interval: list, delta, epsilon, function) -> tuple:
    x_min: float
    iterations = 0
    while abs(interval[1] - interval[0]) >= epsilon:
        iterations += 1
        y_k = (sum(interval) - delta) / 2
        z_k = (sum(interval) + delta) / 2
        if function(y_k) < function(z_k):
            interval[1] = z_k
        else:
            interval[0] = y_k
    else:
        x_min = sum(interval) / 2
    convergence = 1 / (pow(2, iterations / 2))
    return ("x_min = " + str(x_min), "f(x_min) = " + str(function(x_min)), "interval = " + str(interval),
            "iterations = " + str(iterations), "convergence = " + str(convergence))


f = lambda x: 2 * x ** 2 - 2 * x + 3 / 2
L = [-2, 8]
eps = 0.2
l = 0.5
print(dichotomy_find_min(L, eps, l, f))

x = numpy.arange(L[0]-1, L[1]+1, 0.01)
plot.plot(x, f(x))
plot.show()