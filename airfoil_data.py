import os
import subprocess as sp
import numpy as np



def Coefs(alpha, Re, nperfil):
    alpha_i = alpha
    alpha_f = alpha
    alpha_step = 1
    n_iter = 100

    if os.path.exists(nperfil + '.txt'):
        os.remove(nperfil + '.txt')

    input_file = open("input_file.in", 'w')
    input_file.write("LOAD {0}.dat\n".format(nperfil))
    input_file.write(nperfil + '\n')
    input_file.write("PANE\n")
    input_file.write("OPER\n")
    input_file.write("Visc {0}\n".format(Re))
    input_file.write("PACC\n")
    input_file.write("{0}.txt\n\n".format(nperfil))
    input_file.write("ITER {0}\n".format(n_iter))
    input_file.write("ASeq {0} {1} {2}\n".format(alpha_i, alpha_f, alpha_step))
    input_file.write("\n\n")
    input_file.write("quit\n")
    input_file.close()
    sp.call("xfoil.exe < input_file.in", shell=True)
    
    # remove linhas iniciais do txt
    jureg = 12 # número de linhas removidas
    with open(nperfil+".txt", "r") as f:
        lines = f.readlines()
    del lines[:jureg]
    with open(nperfil+".txt", "w") as f:
        for line in lines:
            f.write(line)
    Coefs = np.loadtxt(nperfil+'.txt', skiprows=0)
    return Coefs
'''
nperfil = 'NACA2412'
alpha_i = 5
alpha_f = 5
alpha_step = 1
Re = 1000000
n_iter = 100
Coefs = Coefs(alpha_i, alpha_f, alpha_step, Re, nperfil, n_iter)
print(Coefs)
# print(Clfun(alpha_i, alpha_f, alpha_step, Re, nperfil, n_iter))
'''
'''
Pra se situar no txt:
    alpha   Cl   Cd    Cdp   Cm   Top_Xtr   Bot_Xtr
'''