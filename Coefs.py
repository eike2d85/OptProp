from xfoil_init_airfoil import xfoil_init_airfoil
import numpy as np

# Airfoil Simulation Parameters
Re_min = 5e3
Re_max = 3e6
Re_step =5e4
alpha_i = 0
alpha_f = 20
alpha_step = 1
n_iter = 100


H_bisco_Re = np.linspace(Re_min, Re_max, Re_step)
H_bisco_alpha = np.linspace(alpha_i,alpha_f,alpha_step)

def Coefs(nperfil):
    Cl_data, Cd_data, Cdp_data = xfoil_init_airfoil(nperfil,Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter)
    
    Cl = 2
    local_data = 2

    return local_data