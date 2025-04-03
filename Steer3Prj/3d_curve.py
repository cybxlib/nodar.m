import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def frenet_serret(l_values, curvature_func, torsion_func):
    """
    Calculates a 3D curve using the Frenet-Serret formulas.

    Args:
        l_values: Array of arc length values.
        curvature_func: Function that returns curvature as a function of arc length.
        torsion_func: Function that returns torsion as a function of arc length.

    Returns:
        Arrays of x, y, and z coordinates of the curve.
    """

    T = np.array([1.0, 0.0, 0.0])  	# Initial tangent vector
    N = np.array([0.0, 1.0, 0.0])  	# Initial normal vector
    B = np.cross(T, N)  	    	# Initial binormal vector
    P = np.array([0.0, 0.0, 0.0])  	# Initial position

    x_values = [P[0]]
    y_values = [P[1]]
    z_values = [P[2]]

    for l in l_values[1:]:
        dl = l - l_values[l_values.tolist().index(l)-1]
        kappa = curvature_func(l)
        tau = torsion_func(l)

        dT_dl = kappa * N
        dN_dl = -kappa * T + tau * B
        dB_dl = -tau * N

        T += dT_dl * dl
        N += dN_dl * dl
        B += dB_dl * dl

        # Normalize the vectors
        T /= np.linalg.norm(T)
        N /= np.linalg.norm(N)
        B /= np.linalg.norm(B)

        P += T * dl
        x_values.append(P[0])
        y_values.append(P[1])
        z_values.append(P[2])

    return np.array(x_values), np.array(y_values), np.array(z_values)

# Example Usage:
if __name__ == "__main__":
    l_values = np.linspace(0, 10 * np.pi, 500)  # Arc length values
    
        # Example curvature and torsion functions (helix)    --спираль
    curvature = lambda l: 1.0
    torsion = lambda l: 0.05

    x, y, z = frenet_serret(l_values, curvature, torsion)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Curve (Helix Example)')
    plt.show()
    
    # Example curvature and torsion functions (scrwe)    --винт
    curvature = lambda l: l * 0.1
    torsion = lambda l: 0.05

    x, y, z = frenet_serret(l_values, curvature, torsion)

    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Curve (Scrwe Example)')
    plt.show()

    #Example circle in 3D (planar circle, torsion = 0)  --круг
    curvature_circle = lambda l: 1.0
    torsion_circle = lambda l: 0.0
    x_circle, y_circle, z_circle = frenet_serret(l_values, curvature_circle, torsion_circle)

    figCircle = plt.figure()
    axCircle = figCircle.add_subplot(111, projection='3d')
    axCircle.plot(x_circle, y_circle, z_circle)
    axCircle.set_xlabel('X')
    axCircle.set_ylabel('Y')
    axCircle.set_zlabel('Z')
    axCircle.set_title("3D circle")
    plt.show()

    #Example straight line in 3d space.  --прямая
    curvature_straight = lambda l: 0.0
    torsion_straight = lambda l: 0.0
    x_straight, y_straight, z_straight = frenet_serret(l_values, curvature_straight, torsion_straight)

    figStraight = plt.figure()
    axStraight = figStraight.add_subplot(111, projection = '3d')
    axStraight.plot(x_straight, y_straight, z_straight)
    axStraight.set_xlabel('X')
    axStraight.set_ylabel('Y')
    axStraight.set_zlabel('Z')
    axStraight.set_title("Straight Line in 3D")
    plt.show()
