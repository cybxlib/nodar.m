import numpy as np
import math

def get_f(arg, R):
    """
    Returns a function f(l) based on the chosen parameter `arg`.
    """
    f_funcs = {
        1: lambda l: 1.0 / R,					# this is circle
        2: lambda l: 2.0 * l + 3.0,    			# spiral
        3: lambda l: 0.5 * l**2 + 2 * l + 1,
        4: lambda l: 0.5 * l**3 + 2 * l**2 + 1,
        5: lambda l: np.log(l + np.finfo(float).eps),  	# avoid log(0)
        6: lambda l: np.sin(l),				# sin steps
        7: lambda l: np.sin(l) - 0.5,				# like horr 8
        8: lambda l: math.pi / 3 if l in range(100) else 0	# ~ parabola
    }
    # Return the corresponding function or a default function if arg is not found.
    return f_funcs.get(arg, lambda l: 0.5 * l**4 + 2 * l**3 + 4 * l**2 + 1)
