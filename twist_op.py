#!/usr/bin/env python

"""
Twist order parameter

Defined in 
M. Matsumoto, T. Yagasaki, and H. Tanaka, to be submitted to J. Chem. Phys. (2019).

"""
__version__ = "0.1"


import numpy as np
from collections import defaultdict
# from math import atan2
# import cmath
# import logging

def torsion3(v1,v2,v3):
    """
    Calculate exp 3iA where A is the torsional angle.

                     .       O
                     |     /
                     n3  v3
                     | /
            O---v2---O
          / |
        v1  n1
      /     |
    O       .

    v1,v2,v3 must be normalized to length 1.
    """
    # logger = logging.getLogger()
    n1 = v1 - np.dot(v1,v2)*v2
    L1 = np.linalg.norm(n1)
    n1 /= -L1
    n3 = v3 - np.dot(v2,v3)*v2
    L3 = np.linalg.norm(n3)
    n3 /= L3
    sine   = np.dot(np.cross(n1, n3), v2)
    cosine = np.dot(n1,n3)
    sin3   = 3*sine - 4*sine**3
    cos3   = 4*cosine**3 - 3*cosine
    # angle = atan2(sine,cosine)
    # logger.info((cmath.exp(angle*3j), cos3 + 1j*sin3))
    return cos3 + 1j*sin3



def twist_iter(pairs, vecs):
    """
    calculate twist OP.

    pairs: index pairs for hydrogen bonded pairs. (directed graph)
        shape: (NPAIRS, 2)
        type:  int
    vecs: normalized relative vectors for the corresponding pairs.
        shape: (NPAIRS, 3)
        type: float

    Returns: a generator that yields a pair and a valid twist op.
    """
    vecd = defaultdict(dict)
    for pair, vec in zip(pairs, vecs):
        i, j = pair
        assert j not in vecd[i]
        vecd[i][j] = vec
        assert i not in vecd[j]
        vecd[j][i] =-vec
    for pair in pairs:
        i,j = pair
        # combinations of tortional angles
        L = (len(vecd[i])-1)*(len(vecd[j])-1)
        if L > 0:
            sum = 0.0
            for k in vecd[i]:
                if k != j:
                    for l in vecd[j]:
                        if l != i:
                            sum += torsion3(vecd[k][i], vecd[i][j], vecd[j][l])
            yield pair, sum / L




#
# DEMO: A small ice Ih crystal
#
cell='15.64567753 14.70714529 9.03651852'
waters="""
    0.0846    0.1221    0.3728
    0.3356    0.3066    0.1223
    0.4192    0.3688    0.3712
    0.3356    0.3078    0.6209
    0.1671    0.0594    0.6226
    0.1699    0.3719    0.6205
    0.3339    0.1190    0.1235
    0.3339    0.1202    0.6221
    0.0863    0.3110    0.8701
    0.0863    0.3097    0.3716
    0.1699    0.3707    0.1219
    0.1671    0.0582    0.1240
    0.4165    0.0563    0.3733
    0.4165    0.0575    0.8717
    0.4193    0.3701    0.8696
    0.0846    0.1234    0.8713
    0.5846    0.1221    0.3728
    0.8356    0.3066    0.1223
    0.9192    0.3688    0.3712
    0.8356    0.3078    0.6209
    0.6671    0.0594    0.6226
    0.6699    0.3719    0.6205
    0.8339    0.1190    0.1235
    0.8339    0.1202    0.6221
    0.5863    0.3110    0.8701
    0.5863    0.3097    0.3716
    0.6699    0.3707    0.1219
    0.6671    0.0582    0.1240
    0.9165    0.0563    0.3733
    0.9165    0.0575    0.8717
    0.9193    0.3701    0.8696
    0.5846    0.1234    0.8713
    0.0846    0.6221    0.3728
    0.3356    0.8066    0.1223
    0.4192    0.8688    0.3712
    0.3356    0.8078    0.6209
    0.1671    0.5594    0.6226
    0.1699    0.8719    0.6205
    0.3339    0.6190    0.1235
    0.3339    0.6202    0.6221
    0.0863    0.8110    0.8701
    0.0863    0.8097    0.3716
    0.1699    0.8707    0.1219
    0.1671    0.5582    0.1240
    0.4165    0.5563    0.3733
    0.4165    0.5575    0.8717
    0.4193    0.8701    0.8696
    0.0846    0.6234    0.8713
    0.5846    0.6221    0.3728
    0.8356    0.8066    0.1223
    0.9192    0.8688    0.3712
    0.8356    0.8078    0.6209
    0.6671    0.5594    0.6226
    0.6699    0.8719    0.6205
    0.8339    0.6190    0.1235
    0.8339    0.6202    0.6221
    0.5863    0.8110    0.8701
    0.5863    0.8097    0.3716
    0.6699    0.8707    0.1219
    0.6671    0.5582    0.1240
    0.9165    0.5563    0.3733
    0.9165    0.5575    0.8717
    0.9193    0.8701    0.8696
    0.5846    0.6234    0.8713
"""
cell = np.diag(np.fromstring(cell, dtype=np.float, sep=' '))
waters = np.fromstring(waters, dtype=np.float, sep=' ')
waters = waters.reshape([64,3])



def test(cell, waters):
    N = waters.shape[0]
    # prepare HB vectors
    pairs = []
    vecs = []
    for i in range(N):
        for j in range(i+1, N):

            # displacement vector in relative coordinate
            rel = waters[j] - waters[i]

            # Periodic boundary condition
            rel -= np.floor( rel + 0.5 )

            # relative to absolute coordinate
            d = np.dot(rel, cell)

            # distance
            L = np.linalg.norm(d)

            # if O-O is closer than 3 \AA,
            if L < 3: 
                pairs.append([i,j])
                # normalized displacement vector
                vecs.append(d/L)
    vecs  = np.array(vecs)
    for pair, twist in twist_iter(pairs, vecs):
        print(pair, twist)



if __name__ == "__main__":
    test(cell, waters)
        
    
    
