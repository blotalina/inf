import math
import pylab
from matplotlib import mlab

tmin = -20.0
tmax = 20.0

dx = 0.01
tlist = mlab.frange (tmin, tmax, dx)

pylab.ion()

for a in range (50):
    ylist = [math.cos (2*t) for t in tlist]
    xlist = [math.sin(t+a/10) for t in tlist]
    pylab.clf()
    pylab.plot (xlist, ylist)
    pylab.draw()
    pylab.pause(0.3)


pylab.close()