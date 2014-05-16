from integrate import integrate

def main():
    f = lambda x: x**3 - 2*x**2 + 5
    print integrate(f, 3, 5)
