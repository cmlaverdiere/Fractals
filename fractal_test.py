# Mandelbrot set!

import Image, ImageDraw, math

def trans(v, lmin, lmax, rmin, rmax):
    lspan = lmax - lmin
    rspan = rmax - rmin
    vs = float(v - lmin) / float(lspan)
    return rmin + (vs * rspan)

dimx = dimy = 400
img = Image.new("RGB", (dimx, dimy))
draw = ImageDraw.Draw(img)

f = lambda z, c: z*z - (1-1.619)
max_iters = 100
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

        shift = dimx / 3
        coord_x = (a*shift) + (dimx/1.5)
        coord_y = (b*shift) + (dimy/2)

        if iters == max_iters:
            color_r = iters * trans(coord_x, 0, 255, 1, 5)
            color_g = iters * trans(coord_y, 0, 255, 1, 5)
            color_b = iters * trans(abs(coord_x - coord_y), 0, 255, 1, 5)
        else:
            color_r = iters * 10
            color_g = iters * 10
            color_b = iters * 255

        draw.point((coord_x, coord_y), 
                    fill="rgb(%d, %d, %d)" % (color_r, color_g, color_b))

del draw
img.save("resultT.png");
