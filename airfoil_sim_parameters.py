# Airfoil Simulations Parameters

Re_min = 4000
Re_max = 1205000
Re_step =200000
alpha_i = 0
alpha_f = 20
alpha_step = 1
n_iter = 100
airfoil_list = ['NACA2412']
qtd_airfoil = (len(airfoil_list))

def airfoil_sim_parameters():

    return Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter,airfoil_list
