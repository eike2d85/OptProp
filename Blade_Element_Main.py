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
Div.L(Airplane Propellers - H.Glauert)

'''
# Airfoil Simulations Parameters
'''
Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list = airfoil_sim_parameters()

generate_data = 0

if generate_data == 1:
    data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list)


Parameters = prop_input.prop_input()
B = Parameters[0] # Numero de pás
D = Parameters[1] # Diametro da hélice
R = Parameters[2] # Raio da hélice
R_hub = Parameters[3] # Raio do cubo
R_root = Parameters[4] # Raio da região estrutural
RPM = Parameters[5] 
omega = Parameters[6]
Vax = Parameters[7] # Velocidade axial da aeronave
alpha = Parameters[8] # Ângulo de ataque da hélice
nperfil = Parameters[9] # perfil da hélice
c = Parameters[10] # vetor das cordas em cada posição
pos_c = Parameters[11] # vetor de posição das cordas ao longo do raio
C = Parameters[12] # coef do polinômio de ajuste das cordas



# PARÂMETROS ATMOSFÉRICOS
rho = 1.225  # em kg/m³
mi = 1.7894e-5  # em kg/m.s
v_som = 340  # em m/s
'''

def Blade_Element_Main(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho,Opt_activate):
    
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

    if Opt_activate ==0:
        return T,Q
    else:
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


