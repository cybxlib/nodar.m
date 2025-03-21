    Returns a function f(l) based on the chosen parameter `arg` between 1 and 5

    f_funcs = {
        1: lambda l: 1.0 / R,
        2: lambda l: 2.0 * l + 3.0,  # l / 2.0,
        3: lambda l: np.log(l + np.finfo(float).eps),  # avoid log(0)
        4: lambda l: 0.5 * l**2 + 2 * l + 1,
        5: lambda l: 0.5 * l**3 + 2 * l**2 + 1
        6: lambda l: math.sin(l),
        7: lambda l: math.sin(l) - 0.5
    }
   Return the corresponding function or a default function if arg is > 5.
    return f_funcs.get(arg, lambda l: 0.5 * l**4 + 2 * l**3 + 4 * l**2 + 1)
