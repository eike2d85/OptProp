import numpy as np
import prop_input
import math
import matplotlib.pyplot as plt
from scipy import integrate 
from be_calc import be_calc
from prop_plot import prop_plot
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters



def Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,Beta,nperfil,C,v_som,mi,rho,P_disp,n, Corda_input_v, pos_c, Beta_input_v):
    D = 2*R
    r_step = (R-R_root)/20
    i = 0 
    r = []
    dT_v = []
    dQ_v = []
    beta_v = []
    phi_v =[]
    alpha_v =[]
    corda_v=[]
    a_v = []
    a_linha_v = []
    r.append(R_root)
    while True:
        # beta,dT,dQ,corda = be_calc(v_som,mi,rho,r[i],Vax,omega,Beta,nperfil,B,C)
        dT,dQ,corda,beta, phi, a, a_linha,alpha = be_calc(v_som,mi,rho,r[i],Vax,omega,Beta,nperfil,B,C,R, R_hub)
        dT_v.append(dT)
        dQ_v.append(dQ)
        beta_v.append(beta)
        corda_v.append(corda)
        phi_v.append(phi)
        alpha_v.append(alpha)
        a_v.append(a)
        a_linha_v.append(a_linha)
        if r[i]>=R or len(r)==21:
            break
        r.append(r[i]+r_step)
        i=i+1
    T = integrate.simpson(dT_v, r)
    if math.isnan(T):
        T=0.01
    Q = integrate.simpson(dQ_v, r)
    Ct = T/(rho*n**2*D**4)
    Cp = P_disp/(rho*n**3*D**5)
    J = Vax/(n*D)
    eff = Ct*J/Cp
    
    if Q*omega>P_disp:
        eff = 1e-10 # Penalização por passar do torque que o motor pode fornecer.
        print('penalizei por passar do torque disponível')
    
    for verify_corda in r:
        if C(verify_corda)< C(R):
            eff = 1e-10
            #print("penalizei por ter corda pequena")
            break

    for verify_alpha in alpha_v:
        if verify_alpha> 15*np.pi/180 or verify_alpha<0:
            eff = 1e-10
            #print("penalizei por ter alpha muito grande")
            break


    global eff_max
    if 'eff_max' not in globals():
        print('eff_max não tava aqui')
        eff_max = eff
        prop_plot(C, r, R_hub, R_root, beta_v, T, Q, eff, Corda_input_v, pos_c, Beta_input_v, R)
    else:
        if eff > eff_max:
            eff_max = eff
            print(f"eff_max: {eff_max}")
            print("Achei uma hélice melhor")
            prop_plot(C, r, R_hub, R_root, beta_v, T, Q, eff, Corda_input_v, pos_c, Beta_input_v, R)

    eff_inv = 1/eff
    return eff_inv,T, Q


