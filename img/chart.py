#!/usr/bin/python

import matplotlib.pyplot as plt
from pylab import *

def plot():
  sizes = [296, 356, 444, 590, 884, 1766, 8188, 17634, 29388, 44080]
  newtimes = [6005, 8637, 14314, 25228, 53944, 212050, 5438505, 22058626, 111730697, 221740796]
  newtimesscaled = [x / 1000000 for x in newtimes]
  oldtimes = [12463, 19156, 29957, 52704, 112092, 431725, 10851304, 48938869, 225041224, 462334313]
  oldtimesscaled = [x / 1000000 for x in oldtimes]
  plt.plot(sizes, newtimesscaled, marker='o')
  plt.plot(sizes, oldtimesscaled, marker='o')
  plt.xlabel("Transition matrix size")
  plt.ylabel("Elapsed time ($s$)")

  # this is another inset axes over the main axes                                 
  a = axes([0.19, 0.55, .4, .3])                                        
  plt.plot(sizes, oldtimes, marker='o')
  plt.plot(sizes, newtimes, marker='o') 
  plt.ylabel("Elapsed time ($us$)")                                                  
  setp(a, xlim=(0,2000), ylim=(0,440000), xticks=[], yticks=[])
  a.set_xticks([0, 300, 600, 900, 1200, 1500, 1800, 2000])
  a.set_yticks([200000, 400000])
  plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
  plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

  plt.show()

if __name__ == '__main__':
  plot()

"""
NEW method time = 6005 us, with size = 296
OLD method time = 12463 us, with size = 296

NEW method time = 8637 us, with size = 356
OLD method time = 19156 us, with size = 356

NEW method time = 14314 us, with size = 444
OLD method time = 29957 us, with size = 444

NEW method time = 25228 us, with size = 590
OLD method time = 52704 us, with size = 590

NEW method time = 53944 us, with size = 884
OLD method time = 112092 us, with size = 884

NEW method time = 212050 us, with size = 1766
OLD method time = 431725 us, with size = 1766

NEW method time = 5438505 us, with size = 8818
OLD method time = 10851304 us, with size = 8818

NEW method time = 22058626 us, with size = 17634
OLD method time = 48938869 us, with size = 17634

NEW method time = 111730697 us, with size = 29388
OLD method time = 225041224 us, with size = 29388

NEW method time = 221740796 us, with size = 44080
OLD method time = 462334313 us, with size = 44080
"""