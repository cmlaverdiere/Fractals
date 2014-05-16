# Try out newton's method on some simple functions.

from newton import newton

def main():
    f = lambda x: 3*x**2 - 2
    trials = 10
    print newton(f, trials, 7)
