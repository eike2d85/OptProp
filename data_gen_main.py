import os
import numpy as np
import subprocess as sp
import pandas as pd

def data_gen_main(Re_min, Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list):
    a = {}
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
            aoa = pd.DataFrame(np.loadtxt(nperfil +'Re'+ Re_str + '.txt', skiprows=12)[:,0])
            Cl = pd.DataFrame(np.loadtxt(nperfil +'Re'+ Re_str + '.txt', skiprows=12)[:,1])
            Cd =  pd.DataFrame(np.loadtxt(nperfil +'Re'+ Re_str + '.txt', skiprows=12)[:,2])
            Cdp =  pd.DataFrame(np.loadtxt(nperfil +'Re'+ Re_str + '.txt', skiprows=12)[:,3])
            # Re_number = pd.DataFrame([Re] * len(aoa))
            with pd.ExcelWriter(nperfil+'.xlsx', mode='a', if_sheet_exists="overlay") as writer:
                aoa.to_excel(writer,sheet_name=Re_str,startcol=0, index=False, header= False, merge_cells= False)
                Cl.to_excel(writer,sheet_name=Re_str,startcol=1, index=False, header= False, merge_cells= False)
                Cd.to_excel(writer,sheet_name=Re_str,startcol=2, index=False, header= False, merge_cells= False)
                Cdp.to_excel(writer,sheet_name=Re_str,startcol=3, index=False, header= False, merge_cells= False)
                # Re_number.to_excel(writer,sheet_name=Re_str,startcol=4, index=False, header= False, merge_cells= False)
    return            
        

'''           
data_gen_main(Re_min = 5000,
    Re_max = 1205000,
    Re_step =200000,
    alpha_i = 0,
    alpha_f = 20,
    alpha_step = 1,
    n_iter = 100,
    airfoil_list = ['NACA2412','Clark_Y']
    )
'''
