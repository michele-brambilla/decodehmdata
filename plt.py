import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

import matplotlib
matplotlib.use('qt4agg')
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import  axes3d, Axes3D

import sys

fn = 'out'
if sys.argv > 1:
    fn = sys.argv[1]

with open(fn) as f:
    d = np.loadtxt(f,dtype=int)
if d.shape != (128,128):
    d = d.flatten().reshape(d.size/2,2)
    d = d[:16384,1]
    d = d.reshape(128,128)

r = np.array(range(0,128))
X, Y = np.meshgrid(r, r)

fig = plt.figure()
ax = Axes3D(fig)
#d[0,0]=0
surf = ax.plot_surface(X, Y, d,cmap=cm.hot)


plt.show()
