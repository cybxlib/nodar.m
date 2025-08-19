import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from f_s_tensor import f_s
import curve_examples
import curve_plotting

if __name__ == "__main__":
    # l_values = torch.linspace(0, 10 * torch.pi, 500)  # Arc length values
    l_values = torch.linspace(0, 10 * torch.pi, 2500, device='cpu', dtype=torch.float32)

    # Example Usage
    curvature, torsion = curve_examples.straight_line(l_values)
    x_straight, y_straight, z_straight = frenet_serret(l_values, curvature, torsion)
    curve_plotting.plot_curve(x_straight, y_straight, z_straight, "Straight Line in 3D")

    curvature, torsion = curve_examples.circle(l_values)
    x_circle, y_circle, z_circle = frenet_serret(l_values, curvature, torsion)
    curve_plotting.plot_curve(x_circle, y_circle, z_circle, "3D Circle")

    curvature, torsion = curve_examples.helix(l_values)
    x, y, z = frenet_serret(l_values, curvature, torsion)
    curve_plotting.plot_curve(x, y, z, '3D Curve (Helix Example)')

    curvature, torsion = curve_examples.screw(l_values)
    x, y, z = frenet_serret(l_values, curvature, torsion)
    curve_plotting.plot_curve(x, y, z, '3D Curve (Screw Example)')

    curvature, torsion = curve_examples.tourch_cube(l_values)
    x_straight, y_straight, z_straight = frenet_serret(l_values, curvature, torsion)
    curve_plotting.plot_curve(x_straight, y_straight, z_straight, '3D Curve (Cubic Parabola)')
