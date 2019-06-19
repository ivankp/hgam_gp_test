#!/usr/bin/env python

import math, sys
import ivanp_gp
import numpy as np

# https://www.librec.net/datagen.html
xs = [
-7.288352, -6.354489, -6.343246, -5.873644, -4.744751, -4.092581, -3.743588,
-2.788551, -2.173762, -0.897309, 0.500722, 0.770547, 1.009111, 2.386,
2.475254, 4.245013, 4.332956, 4.908614, 5.837199, 6.143407
]
ys = [
-1.753582, -0.048711, 0.030086, 0.244986, -0.815186, -1.223496, -1.173352,
0.388252, 1.405444, 1.691977, -0.13467, -0.743553, -1.022923, -2.69914,
-2.226361, -1.287966, -1.116046, -1.574499, -1.080229, -0.84384
]
us = [ 0.001 for x in xs ]
ts = np.linspace(xs[0],xs[-1],1001).tolist()

def kernel(a, b, hs):
    return hs[0] * math.exp(-0.5*(((a-b)/hs[1])**2))

hs = ivanp_gp.opt(xs,ys,us,kernel,[[1.,0.1],[0.5,0.1]])
print hs

gp = ivanp_gp.regression(xs,ys,us,ts,lambda a,b: kernel(a,b,hs))

print 'regression complete'

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.figure(num=None, figsize=(6.5, 4), dpi=200)
plt.gca().fill_between(
    ts,
    [ m-u for m,u in gp ],
    [ m+u for m,u in gp ],
    color="#dddddd"
)
plt.plot(xs, ys, 'b.', ms=8)
plt.plot(ts, [ m for m,u in gp ], 'r-', lw=2)
# plt.axis([105,160,0,40])
plt.margins(x=0)

plt.savefig('test_opt.pdf', bbox_inches='tight')

