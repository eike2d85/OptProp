import numpy as np
def fixed_inputs():
    # PARÂMETROS ATMOSFÉRICOS
    rho = 1.225  # em kg/m³
    mi = 1.7894e-5  # em kg/m.s
    v_som = 340  # em m/s

    # VARIÁVEIS DE ENTRADA PARA A OTIMIZAÇÃO
    B=3
    R = 0.625
    Vax = 50/3.6
    P_disp = 26.5*745 #potência do motor em [W]
    RPM = 2800 #rpm onde está o pico da curva de potência
    omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
    n = RPM/60 # Velocidade angular em rps
    R_hub=0.065 # raio do cubo
    R_root=0.15 # raio sem atuação aerodinâmica em m

    return rho, mi, v_som, B, Vax, omega, R_hub, R_root, P_disp, R, n