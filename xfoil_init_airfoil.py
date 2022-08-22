from fixed_Re_calc import fixed_Re_calc



def xfoil_init_airfoil(nperfil,Re_min,Re_max,Re_step,alpha_i,alpha_f,alpha_step,n_iter):

    Cl_data = []
    Cd_data = []
    Cdp_data = []    
    for Re in range(Re_min,Re_max,Re_step):
        data = fixed_Re_calc(alpha_i,alpha_f,alpha_step,Re,nperfil,n_iter)
        Cl_data.append(data[:,1])
        Cd_data.append(data[:,2])
        Cdp_data.append(data[:,3])

    return Cl_data,Cd_data,Cdp_data
'''
Cl_data,Cd_data,Cdp_data = xfoil_init_airfoil('NACA2412',5000,1000000,50000,0,20,1,100)
print(Cl_data)
print(Cd_data)
print(Cdp_data)
'''
