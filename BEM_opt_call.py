import numpy as np
from Blade_Element_Main import Blade_Element_Main
# from Optimization_main import Opt_activate,v_som,mi,rho,B,Vax,omega,R_hub,R_root
from airfoil_sim_parameters import airfoil_list
from fixed_inputs import fixed_inputs
from scipy.interpolate import CubicSpline

rho, mi, v_som, B, Vax, omega, R_hub, R_root, P_disp, R  = fixed_inputs()

def BEM_opt_call(solution, solution_idx):
    c=[]
    # R = solution[0]
    alpha = solution[0]*np.pi/180
    nperfil = airfoil_list[solution[1]]
    c.append(solution[2])
    c.append(solution[3])
    c.append(solution[4])
    c.append(solution[5])
    #c.append(solution[6])
    #c.append(solution[7])
    #c.append(solution[8])
    #c.append(solution[9])
    #c.append(solution[10])
    #c.append(solution[11])
    #c = np.array(c) # cordas ao longo do raio
    #pos_c = np.array([(R_root/R),0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]) # posição das cordas em % do raio
    pos_c = np.array([(R_root/R),0.4,0.7,1])
    pos_c = pos_c * R # posição real das cordas ao longo do raio em m
    # C = np.polyfit(pos_c,c,3) # coef. do polinômio Corda em função do raio
    C = C = CubicSpline(pos_c, c, bc_type='not-a-knot')

    obj, T, Q = Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho,P_disp)
    eff = 1/obj
    helice = {
            "inputs": solution,
            "Vax": Vax,
            "omega": omega,
            "R_hub": R_hub,
            "R_root": R_root,
            "eff":  eff,
            "T": T,
            "Q": Q
    }

    global helices_list
    if 'helices_list' not in globals():
        helices_list = []
        helices_list.append(helice)
    else:
        helices_list.append(helice)
        
    return obj