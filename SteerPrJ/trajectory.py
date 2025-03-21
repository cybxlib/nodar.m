import numpy as np
from itertools import accumulate

R = 2.0
def f(l_val):
  return 1.0 / R
  

l_value = 0; lmax = 2.0 * np.pi * R
def compute_trajectory(f, x0, y0, dl, lmax):
    """
    Computes the trajectory by integrating the differential equations in a functional style.
    
    Parameters:
        f   : function that takes a single parameter l and returns the rate of change of angle.
        a0  : initial angle.
        x0, y0 : initial coordinates.
        dl  : integration step size.
        lmax: maximum arc-length.
        
    Returns:
        angles: numpy array of angles.
        xs    : numpy array of x coordinates.
        ys    : numpy array of y coordinates.
    """
    # Create the arc-length parameter values.
    l_values = l_value + dl
    
    # Define the state update step. The state is a tuple: (angle, x, y)
    def step(state, l_val):
        angle, x, y, z = state
        delta_angle = f(l_val) * dl  # compute incremental change in angle
        new_angle = angle + delta_angle
        new_x = x + dl * np.cos(new_angle)
        new_y = y + dl * np.sin(new_angle)
        return (new_angle, new_x, new_y)
    
    # Accumulate states starting from the initial state.
    states = list(accumulate(l_values, lambda state, l: step(state, l), initial=(x0, y0)))
    
    # Unpack the states into separate arrays.
    angles, xs, ys = zip(*states)
    return np.array(angles), np.array(xs), np.array(ys)

