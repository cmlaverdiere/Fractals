# Integration of a function.
def integrate(f, l, u):
    isum = 0
    dx = .001
    x = l
    while x < u:
        x += dx
        isum += f(x) * dx
    return isum
