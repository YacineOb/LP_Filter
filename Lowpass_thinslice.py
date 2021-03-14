import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

import numpy as np
import pandas as pd
import scipy.signal


f, (ax, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)



ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)
ax3.spines['bottom'].set_visible(False)
ax3.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    labelbottom=False) # labels along the bottom edge are off

ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)
######################################################################################

with open('DAPI.csv') as csv_file:
    data = np.genfromtxt("DAPI.csv", delimiter=",", names=["x", "y"])
data['y'][0] = np.mean(data['y'][1:])
yhat = scipy.signal.savgol_filter(data['y'], 121, 5)
ax.plot(data['x'], data['y'],'b',linewidth = 0.5,label="Gray value")
ax.plot(data['x'], yhat,'black',label="LP filtered")


with open('Calbindin.csv') as csv_file:
    data = np.genfromtxt("Calbindin.csv", delimiter=",", names=["x", "y"])
data['y'][0] = np.mean(data['y'][1:])
yhat = scipy.signal.savgol_filter(data['y'], 121, 5)
ax4.plot(data['x'], yhat,'black')
ax4.plot(data['x'], data['y'],'r',linewidth = 0.5)

with open('TRPC4GFP.csv') as csv_file:
    data = np.genfromtxt("TRPC4GFP.csv", delimiter=",", names=["x", "y"])
data['y'][0] = np.mean(data['y'][1:])
yhat = scipy.signal.savgol_filter(data['y'], 121, 5)
ax3.plot(data['x'], yhat,'black')
ax3.plot(data['x'], data['y'],'g',linewidth = 0.5)

with open('TRPC5.csv') as csv_file:
    data = np.genfromtxt("TRPC5.csv", delimiter=",", names=["x", "y"])
data['y'][0] = np.mean(data['y'][1:])
yhat = scipy.signal.savgol_filter(data['y'], 121, 5)
ax2.plot(data['x'], data['y'],'m',linewidth = 0.5)
ax2.plot(data['x'], yhat,'black')



# Get the bounding box of the original legend
leg = ax.legend(loc="upper center",frameon = False, ncol=2)
bb = leg.get_bbox_to_anchor().inverse_transformed(ax.transAxes)

# Change to location of the legend.
xOffset = 0.3
bb.y0 += xOffset
bb.y1 += xOffset
leg.set_bbox_to_anchor(bb, transform = ax.transAxes)




plt.show()