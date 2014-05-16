# Mandelbrot set!

import Image, ImageDraw, math

dimx = dimy = 400
img = Image.new("RGB", (dimx, dimy))
draw = ImageDraw.Draw(img)

f = lambda z, c: z*z + c
max_iters = 50
epsilon = .005
bound = int(2 / epsilon)

for a in [x * epsilon for x in range(-bound, bound)]:
    for b in [y * epsilon for y in range(-bound, bound)]:
        iters = 0
        c = a + complex(0, b)
        z = 0 + 0j
        while abs(z) < 2 and iters < max_iters:
            iters += 1
            z = f(z, c)

        # Calculate pixel plotting values.
        shift = dimx / 3
        coord_x = (a*shift) + (dimx/1.5)
        coord_y = (b*shift) + (dimy/2)
        draw.point((coord_x, coord_y), 
                    fill="rgb(%d, %d, %d)" % (5*iters,5*iters,5*iters))

del draw
img.save("result2.png");
