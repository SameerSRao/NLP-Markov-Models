from matrix import *

V = [
        [0,1,.5,0],
        [0,0,1,0],
        [1,1,1,1]
    ]

M = [
  [-1,  0,  2],
  [0,  1,  0],
  [0,  0,  1]
]

M2 = [
    [2, 4, 7, 0],
    [2, 6, 8, 2],
    [6, 5, 8, 3]
    ]
#transform(M,V)
M2 = rref(M2)
mPrint(M2)
