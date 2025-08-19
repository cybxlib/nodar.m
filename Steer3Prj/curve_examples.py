import torch

def straight_line(l_values):
    """Defines curvature and torsion for a straight line."""
    curvature = lambda l: torch.tensor(0.0)
    torsion = lambda l: torch.tensor(0.0)
    return curvature, torsion

def circle(l_values):
    """Defines curvature and torsion for a circle."""
    curvature = lambda l: torch.tensor(1.0)
    torsion = lambda l: torch.tensor(0.0)
    return curvature, torsion

def helix(l_values):
    """Defines curvature and torsion for a helix."""
    curvature = lambda l: torch.tensor(1.0)
    torsion = lambda l: torch.tensor(0.05)
    return curvature, torsion

def screw(l_values):
    """Defines curvature and torsion for a screw curve."""
    curvature = lambda l: l * 0.1
    torsion = lambda l: torch.tensor(0.05)
    return curvature, torsion

def tourch_cube(l_values):
   """Defines curvature and torsion 0.5 * l**3 + 2 * l**2 + 1"""
   curvature = lambda l: 0.5 * l**3 + 2 * l**2 + 1
   torsion = lambda l: torch.tensor(1.0)
   return curvature, torsion
