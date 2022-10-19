import numpy as np
from airfoil_data_get import airfoil_data_get

def be_calc(v_som,mi,rho,r,Vax,omega,alpha,nperfil,B,C):
    Vr = omega*r  # em m/s
    W = (Vr**2 + Vax**2)**0.5 
    if (W/v_som)>0.8:
        print('Mach>0.8 quando raio=',r)
    phi = np.arctan(Vax/Vr)  
    theta = phi+alpha 
    # corda = np.polyval(C,r) 
    corda = C(r)
    Re = rho*W*corda/mi  # tem que ver pq devia ser corda média aerodinamica
    Cl,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re)
    # print('peguei os dados', Cl, Cd, Cdp)
    # print('no reynolds %.3f  e alpha %.3f' %(Re,alpha*180/np.pi))
    Cd = Cd + Cdp

    dT=0.5*B*corda*rho*W**2*(Cl*np.cos(phi)-Cd*np.sin(phi)) 
    dQ=0.5*B*corda*r*rho*W**2*(Cl*np.sin(phi)+Cd*np.cos(phi)) 

    return theta,dT,dQ,corda