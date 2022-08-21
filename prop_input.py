import math
import numpy as np
B=2 # Número de Pás
D=0.31 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.01 # raio do cubo
R_root=0.015 # raio sem atuação aerodinâmica em m
RPM=14000 # Velocidade angular em RPM
omega=2*math.pi*RPM/60 # Velocidade angular em Rad/s
Vax=1 # Velocidade axial em m/s
alpha=5 # angulo de ataque em graus
alpha=alpha*math.pi/180
nperfil='NACA2412'
c = np.array([0.02, 0.028, 0.03, 0.028, 0.025, 0.020, 0.016, 0.013, 0.011, 0.01]) # cordas ao longo do raio
pos_c = np.array([(R_root/R),0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])# posição das cordas em % do raio
pos_c = pos_c * R # posição real das cordas ao longo do raio em m
C = np.polyfit(pos_c,c,5) # coef. do polinômio Corda em função do raio
c = np.polyval(C,pos_c) # cordas ao longo do raio após ajuste polinomial em m


def prop_input():
    Parameters = [B, D, R, R_hub, R_root, RPM, omega, Vax, alpha, nperfil, c, pos_c, C]
    return Parameters