import torch

def helix(l):
    """Defines curvature and torsion for a helix."""
    v = torch.tensor(1.)
    tv = torch.tensor(0.05)
    return lambda l: v, lambda l: tv

def screw(l):
    """Defines curvature and torsion for a screw curve."""
    v  = lambda l: l * 0.1
    tv = torch.tensor(0.05)
    return v, lambda l: tv

def circle(l):
    """Defines curvature and torsion for a circle."""
    v = torch.tensor(1.)
    tv = torch.tensor(0.)
    return lambda l: v, lambda l: tv

def straight_line(l):
    """Defines curvature and torsion for a straight line."""
    v = torch.tensor(0.)
    tv = torch.tensor(0.)
    return lambda l: v, lambda l: tv
