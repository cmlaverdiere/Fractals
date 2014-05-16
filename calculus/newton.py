from diff import diff

# Function, Trials, X guess
# Returns the approximated root, and the depth reached.
def newton(f, t, x):
    epsilon = .001
    for i in range(t):
        prev_x = x
        x = x - (f(x) / diff(f, x))
        if abs(x - prev_x) < epsilon:
            return x, i
    return x, t
