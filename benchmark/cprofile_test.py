"""
python -m cProfile -o out.cprof cprofile_test.py
pyprof2calltree -k -i out.cprof &

"""

#[i*i for i in range(10000)]


import numpy as np
x = np.random.rand(20,30)
y = np.random.rand(30,20)
print(np.matmul(x,y).shape)


