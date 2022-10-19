import numpy as np
import matplotlib.pyplot as plt

def prop_plot(C, r, R_hub, R_root, theta_v, T, Q, eff):

    # C_tot = np.polyval(C,r)
    C_tot = C(r)
    C_proj = np.multiply(C_tot,(np.cos(theta_v)))
    C_front = C_proj/4
    C_back = C_proj - C_front
    an = np.linspace(0, 2 * np.pi, 100)
    if plt.fignum_exists(1):
       plt.clf()
    plt.figure(1)
    plt.plot(r,-C_front, label='Leading Edge')
    plt.plot(r, C_back, label='Trailing Edge')
    # plt.plot(R_root * np.cos(an), R_root * np.sin(an), label='Root Radius')
    plt.plot([R_root, R_root], [-R_root, R_root],"--", label='Root Radius')
    plt.plot(R_hub * np.cos(an), R_hub * np.sin(an), label='Hub Radius')
    plt.plot((0,r[len(r)-1]),(0,0))
    plt.text(0,1.5*R_root, "T[N] = %.2f\nQ[Nm] = %.2f\neff = %.2f" %(T,Q,eff), fontsize = 10)
    plt.legend(loc='best')
    plt.axis('equal')
    plt.draw()
    plt.pause(0.1)
    # fig.canvas.draw()
    plt.show(block=False)
    
    # plt.clf()    
    return 

'''
C= [225.728663844678,	-562.853343861536,	202.896040485106,	-28.3024942800284,	1.50949932204858,	0.00302698965582738]
r= [0.0150000000000000,	0.0151000000000000,	0.0152000000000000,	0.0153000000000000,	0.0154000000000000,	0.0155000000000000,	0.0156000000000000,	0.0157000000000000,	0.0158000000000000,	0.0159000000000000]
theta_v = [0.154524615362388,	0.154224088038617,	0.153927507022111,	0.153634795140976,	0.153345877221152,	0.153060680022225,	0.152779132175684,	0.152501164125544,	0.152226708071195,	0.151955697912416]

prop_plot(C, r, 0.01, 0.015, theta_v)
'''