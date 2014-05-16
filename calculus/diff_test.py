from pylab import *
from diff import diff

def main():
    f = lambda x: x**3

    xF = range(-20, 20)
    yF = [f(x) for x in xF]
    yf = [diff(f, x) for x in xF]

    plot(xF, yF)
    plot(xF, yf)
    show()

    print diff(f, 20)
