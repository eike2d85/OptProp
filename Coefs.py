from xfoil_init_airfoil import xfoil_init_airfoil
import numpy as np

# Airfoil Simulation Parameters
Re_min = 5e3
Re_max = 1e6
Re_step =5e4
alpha_i = 0
alpha_f = 20
alpha_step = 1
n_iter = 100

H_bisco_Re = np.arange(Re_min, Re_max, Re_step)
H_bisco_alpha = np.arange(alpha_i,alpha_f,alpha_step)

def Coefs(nperfil, alpha, Re):
    Cl_data, Cd_data, Cdp_data = xfoil_init_airfoil(nperfil,Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter)

    for aoa in H_bisco_alpha:
        if alpha <= aoa:
            aoa_maior = aoa
            aoa_menor = aoa-alpha_step
            for Rey in H_bisco_Re:
                if Re <= Rey:
                    Rey_maior = Rey
                    Rey_menor = Rey - Re_step




    Cl_Re_maior = np.interp([Cl_data[H_bisco_Re.index(Rey_maior)][:],Cl_data[H_bisco_Re.index(Rey_menor)][:]] , [Rey_maior, Rey_menor])
    Cl = 2
    Cd = 2
    local_data = [Cl, Cd]

    return local_data


    CL= Coefs('NACA2412', 5, 557000)
    print(CL)
