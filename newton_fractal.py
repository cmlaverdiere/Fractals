# Newton fractal!
# I'd really like to get this to a higher resolution, but
#   either I'm doing this really inefficiently, or Python
#   is just too slow for this, or both. Maybe I'll move some
#   to c++ later for practice.

import Image, ImageDraw, math
from calculus import newton
from math import pi, sin

dimx = dimy = 512
shift = dimx/2
img = Image.new("RGB", (dimx, dimy))
draw = ImageDraw.Draw(img)

f = lambda z: z**3 - 1
roots = [complex(1, 0), complex(-0.5, sin(2*pi/3)), complex(-0.5, -sin(2*pi/3))]
max_iters = 15
epsilon = .01
bound = int(2 / epsilon)

red = "rgb(255, 0, 0)"
green = "rgb(0, 255, 0)"
blue = "rgb(0, 0, 255)"

for a in range(-dimx/2, dimx/2):
    for b in range(-dimy/2, dimy/2):

        # Apply Newton's method to find our closest root.
        c, depth = newton.newton(f, max_iters, complex(a*epsilon, b*epsilon))

        # Apply shading based on depth of newton function.
        color_depth_mod = 255 / (depth/2 + 1)

        # Decide which color to draw.
        if abs(c - roots[0]) < epsilon:
            draw.point((a+shift, b+shift), fill="rgb(%d, %d, %d)" % (color_depth_mod, 0, 0))
        elif abs(c - roots[1]) < epsilon:
            draw.point((a+shift, b+shift), fill="rgb(%d, %d, %d)" % (0, color_depth_mod, 0))
        elif abs(c - roots[2]) < epsilon:
            draw.point((a+shift, b+shift), fill="rgb(%d, %d, %d)" % (0, 0, color_depth_mod))
        else:
            draw.point((a+shift, b+shift), fill="rgb(255, 255, 0)")

del draw
img.save("results/newton_result3.png");
