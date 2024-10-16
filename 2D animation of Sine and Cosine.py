import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

fig = plt.figure()
l, = plt.plot ([], [], 'k-')
l2, = plt.plot ([],[], 'm--')
plt.xlim(-7, 7)
plt.ylim(-5, 5)

plt.title(' 2D sine & cosine wave animation')

def function(x):
    return np.sin(x)*3

def function2(x):
    return np.cos(x)*3


metadata = dict(title = 'animation', artist = 'Ahmad Shoaib Amiri')
writer = PillowWriter(fps=15, metadata= metadata)

xlist =[]
ylist =[]
ylist2 =[]
with writer.saving(fig, 'sin&cosin2.gif', 100):
     for xval in np.linspace(-7, 7, 100):
         xlist.append(xval)
         ylist.append(function(xval))
         ylist2.append(function2(xval))

         l.set_data(xlist, ylist)
         l2.set_data(xlist, ylist2)
         writer.grab_frame()

