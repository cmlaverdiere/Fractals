from pylab import *

def diff(f, x):
    eps = .001
    return (f(x+eps) - f(x)) / eps

def main():
    f = lambda x: x**3

    xF = range(-20, 20)
    yF = [f(x) for x in xF]
    yf = [diff(f, x) for x in xF]

    plot(xF, yF)
    plot(xF, yf)
    show()

    print diff(f, 20)
