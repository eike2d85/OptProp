import numpy as np
import prop_input
import matplotlib.pyplot as plt
from scipy import integrate 
from be_calc import be_calc

Parameters = prop_input.prop_input()
# globals().update(Parameters)
B = Parameters[0] # Numero de pás
D = Parameters[1] # Diametro da hélice
R = Parameters[2] # Raio da hélice
R_hub = Parameters[3] # Raio do cubo
R_root = Parameters[4] # Raio da região estrutural
RPM = Parameters[5] 
omega = Parameters[6]
Vax = Parameters[7] # Velocidade axial da aeronave
alpha = Parameters[8] # Ângulo de ataque da hélice
nperfil = Parameters[9] # perfil da hélice
c = Parameters[10] # vetor das cordas em cada posição
pos_c = Parameters[11] # vetor de posição das cordas ao longo do raio
C = Parameters[12] # coef do polinômio de ajuste das cordas


# PARÂMETROS ATMOSFÉRICOS
rho = 1.225  # em kg/m³
mi = 1.7894e-5  # em kg/m.s
v_som = 340  # em m/s

r_step = 10**(-3)
i = 0
r = []
dT_v = []
dQ_v = []
r.append(pos_c[0])
while True:
    Vr,W,phi,theta,corda,Re,Cl,Cd,dT,dQ = be_calc(v_som,mi,rho,r[i],Vax,omega,alpha,nperfil,B,C)
    dT_v.append(dT)
    dQ_v.append(dQ)
    if r[i]>=R:
        break
    r.append(r[i]+r_step)
    i=i+1


# r=np.transpose(r)
plt.figure()
plt.plot(r,dT,label='dT x r')
plt.legend(loc='best')
plt.show()

T = integrate.simpson(dT, r)
Q = integrate.simpson(dQ, r)
print('Tração[N]=', T)
print('Torque[N.m]=', Q)