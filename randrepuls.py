# random walk repulsion

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import random

def plot_particles():
    x_1 = 0
    x_2 = 0
    v_1 = 1
    v_2 = -1
    q_1 = 6
    q_2 = 6
    dt = 1
    a = 40
    m_1 = 0.01
    m_2 = 0.01
    pos1 = []
    pos2 = []
    t = 0
    T = 10
    #T = 100000
    #while t<T:
    for i in range(10000):
        plt.clf()
        pos1.append(x_1)
        x_1 = v_1*dt
        pos2.append(x_2)
        x_2 = v_2*dt
        d = np.absolute(x_2-x_1)
        f_dir_1 = -x_2/np.absolute(x_2)
        f_dir_2 = -f_dir_1
        if d<0.1*(t**(1/2)):
            nudge = random.randrange(10,30)
            d = nudge*(t**(1/3))
            x_1 += -nudge*f_dir_1/t
            x_2 += -nudge*f_dir_2/t
        f = a*((q_1*q_2*(np.absolute(v_1*v_2))**(1/2))/d**2)
        a_1 = f*f_dir_1/m_1
        a_2 = f*f_dir_2/m_2
        v_1 += a_1*dt
        if x_1 > 5 or x_1 < -5:
            v_1 += random.randrange(-50,50)*f_dir_1*t**(1/2)
        v_2 += a_2*dt
        if x_2 > 5 or x_2 < -5:
            v_2 += random.randrange(-50,50)*f_dir_2*t**(1/2)
        t+=dt
        time = np.linspace(0,t,t)
        if t % 10 == 0:
            plt.plot(time,pos1,label='particle 1',color = 'orange')
            plt.plot(time,pos2,label='particle 2',color='blue')
            plt.pause(0.001)
            plt.legend()
        i = i - 1
    #print(pos1,pos2)
    plt.plot(time,pos1,label='particle 1')
    plt.plot(time,pos2,label='particle 2')
    plt.legend()
    plt.show()
    #plt.ylim(-100,100)
    return

plot_particles()