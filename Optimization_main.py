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

rho, mi, v_som, B, Vax, omega, R_hub, R_root, P_disp, R, n= fixed_inputs()

# PARÂMETROS DE SIMULAÇÃO DOS PERFIS
Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list = airfoil_sim_parameters()

if generate_data == 1:
    data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list)


'''
bounds = [{'low': 0, 'high': qtd_airfoil},{'low': 0.010, 'high': 0.060},
{'low': 0.010, 'high': 0.060},{'low': 0.005, 'high': 0.050},{'low': 0.005, 'high': 0.040},{'low': 15, 'high': 70},
{'low': 10, 'high': 65},{'low': 5, 'high': 60},{'low': 1, 'high': 40}]
'''
bounds = [{'low': 0, 'high': qtd_airfoil},{'low': 0.030, 'high': 0.150},
{'low': 0.030, 'high': 0.150},{'low': 0.030, 'high': 0.150},{'low': 0.030, 'high': 0.100},{'low': 15, 'high': 70},
{'low': 10, 'high': 65},{'low': 5, 'high': 60},{'low': 1, 'high': 40}]
ga_instance = pygad.GA(num_generations=2000,
                    num_parents_mating=8,
                    fitness_func=BEM_opt_call,
                    sol_per_pop=20,
                    num_genes=9,
                    gene_type=[int, float, float, float, float, float, float, float, float],
                    gene_space=bounds,
                    on_generation=callback_gen,
                    parent_selection_type="sss",
                    keep_parents=-1,
                    crossover_type="single_point",
                    crossover_probability=0.8,
                    mutation_percent_genes=80,
                    mutation_num_genes=5,
                    mutation_type = "random",
                    save_solutions=True,
                    suppress_warnings=True,
                    allow_duplicate_genes=False
                    )
ga_instance.run()
best_solution, best_solution_fitness, best_match_idx = ga_instance.best_solution()
ga_instance.plot_fitness()
ga_instance.plot_genes()
ga_instance.save("pygad_GA")
#print(best_solution)
#print(best_solution_fitness)
helices_list = BEM_opt_call.__globals__["helices_list"]
if os.path.exists('results.txt'): 
            os.remove('results.txt')
with open('results.txt', 'w') as data:
    data.write(str(helices_list))
# print(helices_list)
    
