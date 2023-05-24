import numpy as np
from airfoil_data_get import airfoil_data_get
k = 0.7
def be_calc(v_som,mi,rho,r,Vax,omega,Beta,nperfil,B,C,R,R_hub):
    corda = C(r)
    if corda<0:
        corda = 0.001
    csi = r/R
    Vr = omega*r  # em m/s
    _lambda = Vax/Vr
    sigma = B*corda/(2*np.pi*r)
    jureg = 0
    i = 1
    max_iter = 100
    phi_error = 1
    phi_tolerance = 0.00000001    

    while phi_error > phi_tolerance and i < max_iter:
        if jureg ==0:
            phi = np.arctan(_lambda)
            W = Vax/np.sin(phi) 
        alpha = (Beta(r)*np.pi/180)-phi
        Re = W*corda/mi
        #Cl,Cd,Cdp = airfoil_data_get(nperfil, alpha, Re) # fazer convergir o Cl novo com o Cl inputado
        #Cd = Cd+Cdp
        Cl=0.7
        Cd = 0.02
        #Cl = 0.0887*(alpha*180/np.pi)+0.3497
        #Cd = 0.0024*(alpha*180/np.pi)+0.0178
        Cy=(Cl*np.cos(phi)-Cd*np.sin(phi)) 
        Cx=(Cl*np.sin(phi)+Cd*np.cos(phi)) 
        K = Cy/(4*(np.sin(phi))**2)
        K_linha = Cx/(4*np.cos(phi)*np.sin(phi))
        phi_t = np.arctan(csi*np.tan(phi))
        ft = (B/2)*(1-csi)/(np.sin(phi_t))
        Ft = (2/np.pi)*np.arccos(np.exp(-ft))
        if csi >= 1:
            F = 0
        else:
            F = Ft
        a = sigma*K/(F-(sigma*K))
        #if a < -1:
        #    a = -0.7
        a_linha = sigma*K_linha/(F+(sigma*K_linha))
        if csi >= 1:
            a = 0
            a_linha = 0

        W = np.sqrt((Vax*(1+a))**2 + (Vr*(1-a_linha))**2)

        phi_old = phi
        phi_new = np.arctan((Vax*(1+a))/(Vr*(1-a_linha)))
        phi = (1-k)*phi_old + k*phi_new
        phi_error = abs(phi-phi_old)
        jureg = jureg + 1
        if i == max_iter:
            print('não convergiu o phi quando r/R=', csi)
        i=i+1


    dT = 0.5*rho*W**2*B*corda*Cy
    dQ = 0.5*rho*W**2*B*corda*Cx*r

    if (W/v_som)>0.8:
        print('Mach>0.8 quando raio=',r)

    return dT,dQ,corda,(Beta(r)*np.pi/180), phi*180/np.pi, a , a_linha, alpha