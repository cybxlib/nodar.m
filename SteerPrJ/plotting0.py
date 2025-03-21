import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d
import numpy as np

def plot_trajectory(xs, ys, arg, a0):
    """
    Plots the trajectory using matplotlib.
    
    Parameters:
        xs  : x coordinates.
        ys  : y coordinates.
        arg : the parameter used (for display in the title).
    """
    zs = 2.0
    zs = np.array(zs)
    z = zs.reshape((len(xs), len(ys)))

    ax = plt.figure().add_subplot(projection='3d')
    X, Y, Z = xs, ys, z
    ax.contour(X, Y, Z, cmap=cm.coolwarm)  # Plot contour curves
    plt.show()

