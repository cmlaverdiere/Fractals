# Newton fractal!
# I'd really like to get this to a higher resolution, but
#   either I'm doing this really inefficiently, or Python
#   is just too slow for this, or both. Maybe I'll move some
#   to c++ later for practice.

import Image, ImageDraw, math
from sympy.mpmath import *
from calculus import newton
from math import pi, sin

# Some polynomials to play around with.
ff = lambda z: z**3 - 1
pf = [1, 0, 0, -1]
fg = lambda z: z**3 - 2*z + 2
pg = [1, 0, -2, 2]
fh = lambda z: z**8 + 15*z**4 - 16
ph = [1, 0, 0, 0, 15, 0, 0, 0, -16]

# Choose polynomial / function to use for fractal.
f = fg
p = pg

# Calculate real/complex roots of function using sympy.
roots = []
for r in polyroots(p):
    roots.append(r)

# Drawing constants
dimx = dimy = 512
shift = dimx / 2
img = Image.new("RGB", (dimx, dimy))
draw = ImageDraw.Draw(img)

# Accuracy constants
max_iters = 15
epsilon = .01
bound = int(2 / epsilon)

# Color constants
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
pink = (255, 128, 128)
gray = (128, 128, 128)
brown = (128, 0, 0)
orange = (255, 128, 0)

colors = [blue, red, green, yellow, magenta, pink, gray, brown, orange]

for a in range(-dimx/2, dimx/2):
    for b in range(-dimy/2, dimy/2):

        # Apply Newton's method to find our closest root.
        c, depth = newton.newton(f, max_iters, complex(a*epsilon, b*epsilon))

        # Apply shading based on depth of newton function.
        color_depth_mod = (depth/2 + 1)

        # Decide which color to draw.
        found = False
        for i in range(len(roots)):
            if abs(c - roots[i]) < epsilon:
                dcolor = [c / color_depth_mod for c in colors[i]]
                draw.point((a+shift, b+shift), tuple(dcolor))
                found = True
        if not found:
            draw.point((a+shift, b+shift), fill="rgb(255, 255, 0)")

del draw
img.save("results/newton_result5.png");
