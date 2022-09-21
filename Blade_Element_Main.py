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

def Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho):
    
    r_step = 10**(-3)
    i = 0
    r = []
    dT_v = []
    dQ_v = []
    theta_v = []
    r.append(R_root/R)
    while True:
        theta,dT,dQ = be_calc(v_som,mi,rho,r[i],Vax,omega,alpha,nperfil,B,C)
        dT_v.append(dT)
        dQ_v.append(dQ)
        theta_v.append(theta)
        if r[i]>=R:
            break
        r.append(r[i]+r_step)
        i=i+1
    T = integrate.simpson(dT_v, r)
    Q = integrate.simpson(dQ_v, r)
    # prop_plot(C, r, R_hub, R_root, theta_v)
    eff_inv = Q/T
    return eff_inv
'''
plt.figure(1)
plt.plot(r,dT_v,label='dT x r')
plt.legend(loc='best')


T = integrate.simpson(dT_v, r)
Q = integrate.simpson(dQ_v, r)
print('\nTração[N]=', T)
print('Torque[N.m]=', Q)
'''


