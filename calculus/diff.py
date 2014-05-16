# Differentation of a function.
def diff(f, x):
    eps = .001
    return (f(x+eps) - f(x)) / eps
