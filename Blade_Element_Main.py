import numpy as np
import prop_input
import matplotlib.pyplot as plt
from scipy import integrate 
from be_calc import be_calc
from prop_plot import prop_plot
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters
'''
Programa construido com base na teoria do elemento de pá "Aerodynamic Theory-A General Review of Progress-Vol IV
Div.L(Airplane Propellers - H.Glauert)'''


def Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho,P_disp):
    r_step = 10**(-3)
    i = 0
    r = []
    dT_v = []
    dQ_v = []
    theta_v = []
    corda_v=[]
    r.append(R_root)
    while True:
        theta,dT,dQ,corda = be_calc(v_som,mi,rho,r[i],Vax,omega,alpha,nperfil,B,C)
        dT_v.append(dT)
        dQ_v.append(dQ)
        theta_v.append(theta)
        corda_v.append(corda)
        if r[i]>=R:
            break
        r.append(r[i]+r_step)
        i=i+1
    T = integrate.simpson(dT_v, r)
    Q = integrate.simpson(dQ_v, r)
    eff = T*Vax/P_disp
    global eff_max
    if 'eff_max' not in globals():
        print('eff_max não tava aqui')
        eff_max = eff
    else:
        if eff > eff_max:
            eff_max = eff
            print(f"eff_max: {eff_max}")
            prop_plot(C, r, R_hub, R_root, theta_v, T, Q, eff)
    if Q*omega>0.9*P_disp:
        eff = 1e-5 # Penalização por passar do torque que o motor pode fornecer.
        print('penalizei por passar do torque disponível')

    for verify_corda in r:
        if C(verify_corda)< C(R):
            eff = 1e-5
            print("penalizei por ter corda pequena")
        if eff == 1e-5:
            break
    eff_inv = 1/eff
    return eff_inv,T, Q

'''
plt.figure(1)
plt.plot(r,dT_v,label='dT x r')
plt.legend(loc='best')

print('\nTração[N]=', T)
print('Torque[N.m]=', Q)
'''


