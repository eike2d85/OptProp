from stat import FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
import os
import pygad
import numpy as np
from Blade_Element_Main import Blade_Element_Main as BEM
from fixed_inputs import fixed_inputs
from data_gen_main import data_gen_main
from airfoil_sim_parameters import airfoil_sim_parameters, qtd_airfoil
from BEM_opt_call import BEM_opt_call

def callback_gen(ga_instance):
    print("Generation : ", ga_instance.generations_completed)
    print("Fitness of the best solution :", ga_instance.best_solution()[0])
    return

generate_data = 0

rho, mi, v_som, B, Vax, omega, R_hub, R_root, P_disp, R= fixed_inputs()

# PARÂMETROS DE SIMULAÇÃO DOS PERFIS
Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list = airfoil_sim_parameters()

if generate_data == 1:
    data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list)


'''
bounds = [{'low': 2, 'high': 10}, {'low': 0, 'high': qtd_airfoil},{'low': 0.01, 'high': 0.03},
{'low': 0.01, 'high': 0.03},{'low': 0.025, 'high': 0.04},{'low': 0.025, 'high': 0.04},{'low': 0.02, 'high': 0.035},
{'low': 0.015, 'high': 0.025},{'low': 0.015, 'high': 0.025},{'low': 0.01, 'high': 0.015},{'low': 0.01, 'high': 0.015},
{'low': 0.005, 'high': 0.01}]
'''
bounds = [{'low': 2, 'high': 10}, {'low': 0, 'high': qtd_airfoil},{'low': 0.01, 'high': 0.035},
{'low': 0.005, 'high': 0.035},{'low': 0.005, 'high': 0.035},{'low': 0.005, 'high': 0.015}]
ga_instance = pygad.GA(num_generations=5000,
                    num_parents_mating=2,
                    fitness_func=BEM_opt_call,
                    sol_per_pop=5,
                    num_genes=6,
                    gene_type=[float, int, float, float, float, float],
                    gene_space=bounds,
                    on_generation=callback_gen,
                    parent_selection_type="rank",
                    crossover_type="uniform",
                    crossover_probability=0.8
                    )
ga_instance.run()
best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution()
ga_instance.plot_fitness()
# ga_instance.plot_genes()
ga_instance.save("pygad_GA")
#print(best_solution)
#print(best_solution_fitness)
helices_list = BEM_opt_call.__globals__["helices_list"]
if os.path.exists('results.txt'): 
            os.remove('results.txt')
with open('results.txt', 'w') as data:
    data.write(str(helices_list))
# print(helices_list)
    
