import numpy as np
from Blade_Element_Main import Blade_Element_Main
# from Optimization_main import Opt_activate,v_som,mi,rho,B,Vax,omega,R_hub,R_root
from airfoil_sim_parameters import airfoil_list
from fixed_inputs import fixed_inputs
from scipy.interpolate import CubicSpline

rho, mi, v_som, B, Vax, omega, R_hub, R_root, P_disp, R, n  = fixed_inputs()

def BEM_opt_call(solution, solution_idx):
    c=[]
    Beta=[]
    nperfil = airfoil_list[solution[0]]
    c.append(solution[1])
    c.append(solution[2])
    c.append(solution[3])
    c.append(solution[4])
    Beta.append(solution[5])
    Beta.append(solution[6])
    Beta.append(solution[7])
    Beta.append(solution[8])

    #c = np.array(c) # cordas ao longo do raio
    #pos_c = np.array([(R_root/R),0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]) # posição das cordas em % do raio
    pos_c = np.array([(R_root/R),0.4,0.7,1])
    pos_c = pos_c * R # posição real das cordas e betas ao longo do raio em m
    # C = np.polyfit(pos_c,c,3) # coef. do polinômio Corda em função do raio
    C = CubicSpline(pos_c, c, bc_type='not-a-knot')
    beta = CubicSpline(pos_c, Beta, bc_type='not-a-knot')

    obj, T, Q = Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,beta,nperfil,C,v_som,mi,rho,P_disp,n, c, pos_c, Beta)
    eff = 1/obj


    helice_row = []
    helice = {
            "inputs": solution,
            "B": B,
            "R": R,
            "Vax": Vax,
            "omega": omega,
            "R_hub": R_hub,
            "R_root": R_root,
            "eff":  eff,
            "T": T,
            "Q": Q
    }

    # Iterar sobre as chaves (k) e valores (v) do dicionario
    for k, v in helice.items():
        if type(v) == list: # Se o valor for uma lista, iterar sobre ela
            for input in v:
                helice_row.append(input)
        else:
            helice_row.append(v)


    global helices_list
    if 'helices_list' not in globals():
        helices_list = []
        if eff>0.01: 
            helices_list.append(helice)
    else:
        if eff>0.01:
            helices_list.append(helice)

    global helices_matrix
    if "helices_matrix" not in globals():
        helices_matrix = []
        helices_matrix.append(helice_row)
    else:
        helices_matrix.append(helice_row)
        
    return obj