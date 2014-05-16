def integrate(f, l, u):
    isum = 0
    dx = .001
    x = l
    while x < u:
        x += dx
        isum += f(x) * dx
    return isum

def main():
    f = lambda x: x**3 - 2*x**2 + 5
    print integrate(f, 3, 5)
