import matplotlib.pyplot as plt
import math
import os.path
import numpy as np
def frange(x, y, jump):
    while x < y:
        yield x
        x += jump
dirname = os.path.dirname(__file__)
filename = os.path.join(dirname,'results')
if os.path.exists(filename)==False:
    os.mkdir(filename)
filename = os.path.join(filename, 'results.txt')
with open(filename, 'w') as f:
    xres = []
    fres = []
    for x in frange(-5.12, 5.12, 0.1):
        A = 10
        function = A+math.pow(x, 2)-A*math.cos((2*math.pi*x))
        xres.append('%.4f' % x)
        fres.append('%.4f' % function)
    for i in range(len(xres)):
       f.write(str(xres[i])+"    "+str(fres[i])+"\n")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    xres = list(map(float, xres))
    fres = list(map(float, fres))
    ax.set_xticks(np.arange(-5.12, 5.12, 1 ))
    ax.set_yticks(np.arange(min(fres), max(fres), max(xres)/2))
    ax.plot(xres, fres)
    plt.show()
