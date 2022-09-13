from scipy.optimize import differential_evolution
import numpy as np
from Blade_Element_Main import Blade_Element_Main as BEM
import prop_input
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters, qtd_airfoil
from BEM_opt_call import BEM_opt_call
    
Opt_activate = 1
generate_data = 0

# PARÂMETROS ATMOSFÉRICOS
rho = 1.225  # em kg/m³
mi = 1.7894e-5  # em kg/m.s
v_som = 340  # em m/s

# VARIÁVEIS DE ENTRADA PARA A OTIMIZAÇÃO
B=2
Vax = 1
RPM = 14000
omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
R_hub=0.01 # raio do cubo
R_root=0.015 # raio sem atuação aerodinâmica em m


# PARÂMETROS DE SIMULAÇÃO DOS PERFIS
Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list = airfoil_sim_parameters()

if generate_data == 1:
    data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list)

if Opt_activate ==  0:
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
    

    T,Q = BEM(B,R,R_hub,R_root,omega,Vax,alpha,nperfil,C,v_som,mi,rho,Opt_activate)
    print('Thrust [N]:', T)
    print('Torque {N.m]:', Q)

else:
    bounds = [(0.12,0.16),(2, 12),(0, qtd_airfoil),(0.01, 2*R_hub),(0.01, 0.03),
    (0.025, 0.04),(0.025, 0.04),(0.02,0.035),(0.015, 0.025),(0.015,0.025),(0.01,0.020),(0.01,0.015),(0.005,0.010)]
    result = differential_evolution(BEM_opt_call, bounds, args=(Opt_activate,v_som,mi,rho,B,Vax,omega,R_hub,R_root))
    result.x, result.fun
    print(result)
