import sys
sys.path.append('..');

import MongeAmpere as ma
import numpy as np
import scipy as sp
import scipy.optimize as opt
import matplotlib.pyplot as plt
import matplotlib.tri as tri

X = np.array([[0,0],[1,0],[1,1],[0,1]], dtype=float);
mu = np.ones(4);
dens = ma.Density_2(X,mu);

# target is a random set of points
N = 100;
Y = np.random.rand(N,2);
w = np.zeros(N);

for i in xrange(1,50):
    [Z,m] = ma.lloyd_2(dens, Y, w);
    Y=Z;
    plt.cla();
    T = ma.delaunay_2(Y,w);
    triang = tri.Triangulation(Y[:,0], Y[:,1], T);
    plt.gca().set_aspect('equal')
    plt.triplot(triang, 'bo-')
    plt.pause(.01)
