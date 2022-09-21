import numpy as np
def fixed_inputs():
    # PARÂMETROS ATMOSFÉRICOS
    rho = 1.225  # em kg/m³
    mi = 1.7894e-5  # em kg/m.s
    v_som = 340  # em m/s

    # VARIÁVEIS DE ENTRADA PARA A OTIMIZAÇÃO
    B=2
    Vax = 1
    RPM = 14000
    omega=2*np.pi*RPM/60 # Velocidade angular em Rad/s
    R_hub=0.01 # raio do cubo
    R_root=0.015 # raio sem atuação aerodinâmica em m

    return rho, mi, v_som, B, Vax, omega, R_hub, R_root