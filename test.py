from __future__ import division
import sys
import copy
sys.dont_write_bytecode = True

"""
Testing QDA
"""
def test_QDA():
    from QDA import QDA
    x = [
        [2.95, 6.63],
        [2.53, 7.79],
        [3.57, 5.65],
        [3.16, 5.47],
        [2.58, 4.46],
        [2.16, 6.22],
        [3.27, 3.52],
    ]
    e = copy.deepcopy(x)
    y = [1,1,1,1,2,2,2]
    t = QDA(x, y)
    for i, a in enumerate(e):
        print 'predicted: %d  original: %d' % (t.predict(e[i]), y[i]) 

test_QDA()
