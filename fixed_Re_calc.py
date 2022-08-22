'''import pandas as pd

def xfoil_init_airfoils(nperfil):
    Cl_data = pd.read_excel(nperfil+'.xlsx', sheet_name='Cl')

    return(Cl_data)

Cl = xfoil_init_airfoils('Clark_Y')

print(Cl)'''

import subprocess as sp
import numpy as np

def fixed_Re_calc(alpha_i,alpha_f,alpha_step,Re,nperfil,n_iter):
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
    Coef = np.loadtxt(nperfil+'.txt', skiprows=12)
    return Coef
'''
nperfil = 'NACA2412'
alpha_i = 0
alpha_f = 20
alpha_step = 1
Re = 1000000
n_iter = 100
dados = fixed_Re_calc(alpha_i, alpha_f, alpha_step, Re, nperfil, n_iter)
print(dados[:,1])
'''

# print(Clfun(alpha_i, alpha_f, alpha_step, Re, nperfil, n_iter))

'''
Pra se situar no txt:
    alpha   Cl   Cd    Cdp   Cm   Top_Xtr   Bot_Xtr
'''
