import argparse
import numpy as np
import cmath
from functions import get_f
from trajectory import compute_trajectory
from plotting import plot_trajectory

def main(arg, a0):	# arg = No of function f(l); a0 = initial angle
#    complex(
    # Constants and initial conditions.
    R = 2.0
    x0, y0, x0 = 2.0, 2.0, 2.0  # starting point
    
    dlx, dly = 0.01, 0.02        # integration step size
    dl = complex(dlx, dly)
    
    z0 = 2.0
    lmax = 2 * np.pi * R

    # Retrieve the function based on the chosen argument.
    f = 1.0 / R     # get_f(arg, R)
    
    # Compute the trajectory using a functional approach.
    angles, xs, ys = compute_trajectory(f, x0, y0, dl, lmax)	#f, x0, y0, dl, lmax
    
    # Plot the computed trajectory.
    plot_trajectory(xs, ys, arg, a0)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Compute and plot a trajectory based on the provided function parameter."
    )
    parser.add_argument("--arg", type=int, default=1, help="Parameter to choose which function to use (default: 1)")
    parser.add_argument("--a0", type=float, default=0.0, help="Another parameter (default: 1)")
    args = parser.parse_args()
    main(args.arg, args.a0)

