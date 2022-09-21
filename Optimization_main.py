from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
import pygad
import numpy as np
from Blade_Element_Main import Blade_Element_Main as BEM
from fixed_inputs import fixed_inputs
import prop_input
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters, qtd_airfoil
from BEM_opt_call import BEM_opt_call

def callback_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed)
    print("Fitness of the best solution :", ga_instance.best_solution()[0])
    return

Opt_activate = 1
generate_data = 0


rho, mi, v_som, B, Vax, omega, R_hub, R_root = fixed_inputs()

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
    bounds = [{'low': 0.12, 'high': 0.16}, {'low': 2, 'high': 12}, {'low': 0, 'high': qtd_airfoil},{'low': 0.01, 'high': 2*R_hub},
    {'low': 0.01, 'high': 0.03},{'low': 0.025, 'high': 0.04},{'low': 0.025, 'high': 0.04},{'low': 0.02, 'high': 0.035},
    {'low': 0.015, 'high': 0.025},{'low': 0.015, 'high': 0.025},{'low': 0.01, 'high': 0.015},{'low': 0.01, 'high': 0.015},
    {'low': 0.005, 'high': 0.01}]
    
    ga_instance = pygad.GA(num_generations=100,
                       num_parents_mating=2,
                       fitness_func=BEM_opt_call,
                       sol_per_pop=5,
                       num_genes=13,
                       gene_type=[float, float, int, float, float, float, float, float, float, float, float, float, float],
                       gene_space=bounds,
                       on_generation=callback_gen)
    ga_instance.run()
    # best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution()
    ga_instance.plot_fitness()
    ga_instance.save("pygad_GA")
    # print(best_solution)
    # print(best_solution_fitness)


