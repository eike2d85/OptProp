import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

D=0.31 # Diâmetro em m
R=D/2 # Raio em m
R_hub=0.01 # raio do cubo
R_root=0.015 # raio sem atuação aerodinâmica em m
pos_c = np.array([(R_root/R),0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1])# posição das cordas em % do raio
pos_c = pos_c * R # posição real das cordas ao longo do raio em m
c = np.array([0.02, 0.028, 0.03, 0.028, 0.025, 0.020, 0.016, 0.013, 0.011, 0.01]) # cordas ao longo do raio
C = CubicSpline(pos_c, c, bc_type='not-a-knot')
print('valor:', C(0.1))

plt.figure()
plt.plot(pos_c, C(pos_c))
plt.legend('Cubic Spline')
plt.axis('equal')
plt.title('Cubic-spline interpolation')
plt.show()
