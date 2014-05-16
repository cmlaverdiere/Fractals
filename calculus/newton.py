# Try out newton's method on some simple functions.

from diff import diff

# Function, Trials, X guess
def newton(f, t, x):
    epsilon = .001
    for i in range(t):
        prev_x = x
        x = x - (f(x) / diff(f, x))
        if abs(x - prev_x) < epsilon:
            return x, i
    return x, t

def main():
    f = lambda x: 3*x**2 - 2
    trials = 10
    print newton(f, trials, 7)
