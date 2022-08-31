import os
import numpy as np
import subprocess as sp
import pandas as pd



Re_min = 5000
Re_max = 1205000
Re_step =200000
alpha_i = 0
alpha_f = 20
alpha_step = 1
n_iter = 100


a = {}
b = {}
airfoil_list = ['NACA2412', 'NACA0012','Clark_Y']

for nperfil in airfoil_list:

    for Re in range(Re_min, Re_max+Re_step, Re_step):
        Re_str = str(Re)
        if os.path.exists(nperfil +'Re'+ Re_str + '.txt'): 
            os.remove(nperfil+'Re'+ Re_str + '.txt')
        a['input_'+ nperfil] = open('input_' + nperfil + '.in', 'w')
        a['input_'+ nperfil].write("LOAD {0}.dat\n".format(nperfil))
        a['input_'+ nperfil].write(nperfil + '\n')
        a['input_'+ nperfil].write("PANE\n")
        a['input_'+ nperfil].write("OPER\n")
        a['input_'+ nperfil].write("Visc {0}\n".format(Re))
        a['input_'+ nperfil].write("PACC\n")
        a['input_'+ nperfil].write("{0}Re{1}.txt\n\n".format(nperfil,Re))
        a['input_'+ nperfil].write("ITER {0}\n".format(n_iter))
        a['input_'+ nperfil].write("ASeq {0} {1} {2}\n".format(alpha_i, alpha_f, alpha_step))
        a['input_'+ nperfil].write("\n\n")
        a['input_'+ nperfil].write("quit\n")
        a['input_'+ nperfil].close()
        sp.call('xfoil.exe < input_' + nperfil + '.in', shell=True)
        #temp_data = np.loadtxt(nperfil+'.txt', skiprows=12)
    #temp_data= pd.read_csv(nperfil+'.txt', skiprows=12)
    #print('data_temp:',temp_data)
        


