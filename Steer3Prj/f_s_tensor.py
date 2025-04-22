import torch

def f_s(l_val, v, tv):		#curvature_func, torsion_func):
    """
    Calculates a 3D curve using the Frenet-Serret formulas with PyTorch.

    Args:
        l_values: Tensor of arc length values.
        curvature_func: Function that returns curvature as a function of arc length.
        torsion_func: Function that returns torsion as a function of arc length.

    Returns:
        Tensors of x, y, and z coordinates of the curve.
    """

    T = torch.tensor([0., 1., 0.])
    N = torch.tensor([0., 0., 1.])
    B = torch.linalg.cross(T, N).clone().detach()
    P = torch.tensor([0., 0., 0.])
    
#    print(f"(T= {T} \n N= {N} \n B= {B} \n P= {P})")

    x_values = [P[0].item()]
    y_values = [P[1].item()]
    z_values = [P[2].item()]
   

    for i in range(1, len(l_val)):
        l = l_val[i]
        dl = l - l_val[i - 1]

        dT_dl =  v(l) * N
        dN_dl = -v(l) * T + tv(l) * B
        dB_dl = -tv(l) * N

        T = T + dT_dl * dl
        N = N + dN_dl * dl
        B = B + dB_dl * dl

        # Normalize the vectors
        T = T / torch.linalg.norm(T)
        N = N / torch.linalg.norm(N)
        B = B / torch.linalg.norm(B)

        P = P + T * dl
#        print(f"(T= {T} \n N= {N} \n B= {B} \n P= {P})")    
        x_values.append(P[0].item())
        y_values.append(P[1].item())
        z_values.append(P[2].item())

    return torch.tensor(x_values), torch.tensor(y_values), torch.tensor(z_values)
