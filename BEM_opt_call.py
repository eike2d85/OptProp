import numpy as np
from Blade_Element_Main import Blade_Element_Main
# from Optimization_main import Opt_activate,v_som,mi,rho,B,Vax,omega,R_hub,R_root
from airfoil_sim_parameters import airfoil_list


def BEM_opt_call(opt_input,Opt_activate,v_som,mi,rho,B,Vax,omega,R_hub,R_root):
    c=[]
    R = opt_input[0]
    alpha = opt_input[1]*np.pi/180
    nperfil = airfoil_list[round(opt_input[2])]
    c.append(opt_input[3])
    c.append(opt_input[4])
    c.append(opt_input[5])
    c.append(opt_input[6])
    c.append(opt_input[7])
    c.append(opt_input[8])
    c.append(opt_input[9])
    c.append(opt_input[10])
    c.append(opt_input[11])
    c.append(opt_input[12])

    c = np.array(c) # cordas ao longo do raio
    pos_c = np.array([(R_root/R),0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])# posição das cordas em % do raio
    pos_c = pos_c * R # posição real das cordas ao longo do raio em m
    C = np.polyfit(pos_c,c,5) # coef. do polinômio Corda em função do raio


    obj = Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho,Opt_activate)


    return obj