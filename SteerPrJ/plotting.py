import matplotlib.pyplot as plt

def plot_trajectory(xs, ys, arg, a0):
    """
    Plots the trajectory using matplotlib.
    
    Parameters:
        xs  : x coordinates.
        ys  : y coordinates.
        arg : the parameter used (for display in the title).
    """
    plt.figure(figsize=(8, 6))
    plt.title(f'Graph Plot f(l) = {arg}; start angle = {a0}', fontsize=20, color='blue', fontfamily='serif')
    plt.xlabel("-- Xc --", fontsize=15, color='darkred', fontfamily='serif')
    plt.ylabel("-- Yc --", fontsize=15, color='darkred', fontfamily='serif')
    plt.plot(xs, ys)
    plt.show()

