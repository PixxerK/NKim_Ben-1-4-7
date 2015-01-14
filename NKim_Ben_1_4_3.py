import matplotlib.pyplot as plt 
import os.path as op
import numpy as np

directory = op.dirname(op.abspath(__file__))
filename = op.join(directory, 'cat1-a.gif')
img = plt.imread(filename)

