import numpy as np
from airfoil_data import Coefs


def be_calc(v_som,mi,rho,r,Vax,omega,alpha,nperfil,B,C):
    Vr = omega*r  # em m/s
    W = (Vr**2 + Vax**2)**0.5 
    if (W/v_som)>0.8:
        print('Mach>0.8 quando raio=',r)
    phi = np.arctan(Vax/Vr)  
    theta = phi+alpha 
    corda = np.polyval(C,r) 
    Re = rho*W*corda/mi  # tem que ver pq devia ser corda média aerodinamica
    data = Coefs((theta*180/np.pi),Re,nperfil)
    if len(data)< 1:
        print('EMPTY DATA FROM XFOIL')
        Cl=0
        Cd=0
    else:
        Cl = data[1]
        Cd = data[2] + data[3]

    dT=0.5*B*corda*rho*W**2*(Cl*np.cos(phi)-Cd*np.sin(phi)) 
    dQ=0.5*B*corda*r*rho*W**2*(Cl*np.sin(phi)+Cd*np.cos(phi)) 

    return Vr,W,phi,theta,corda,Re,Cl,Cd,dT,dQ