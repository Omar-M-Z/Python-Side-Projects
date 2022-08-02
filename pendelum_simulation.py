import numpy.distutils.intelccompiler
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

G =    9.81  # acceleration due to gravity, in m/s^2
L1 =    5# length of pendulum 1 in meters
L2 =    20# length of pendulum 2 in meters
M1 =    20 # mass of pendulum 1 in kg
M2 =    3 # mass of pendulum 2 in kg

th1 =  120# initial angle of pendulum 1 (degrees)
th2 =  -100# initial angle of pendulum 2 (degrees)
w1 =  -150 # initial angular velocity of pendulum 1 (degrees per second)
w2 =  20   # initial angular velocity of pendulum 2 (degrees per second)

# create a time array sampled at "dt" second long steps
dt = 0.02
t = np.arange(0, 20, dt)

# initial state
state = np.radians([th1, w1, th2, w2])

# Derivatives
def derivs(state, t):

    dydx = np.zeros_like(state)
    dydx[0] = state[1]

    delta = state[2] - state[0]
    den1 = (M1+M2) * L1 - M2 * L1 * cos(delta) * cos(delta)
    dydx[1] = ((M2 * L1 * state[1] * state[1] * sin(delta) * cos(delta)
                + M2 * G * sin(state[2]) * cos(delta)
                + M2 * L2 * state[3] * state[3] * sin(delta)
                - (M1+M2) * G * sin(state[0]))
               / den1)

    dydx[2] = state[3]

    den2 = (L2/L1) * den1
    dydx[3] = ((- M2 * L2 * state[3] * state[3] * sin(delta) * cos(delta)
                + (M1+M2) * G * sin(state[0]) * cos(delta)
                - (M1+M2) * L1 * state[1] * state[1] * sin(delta)
                - (M1+M2) * G * sin(state[2]))
               / den2)

    return dydx

y = integrate.odeint(derivs, state, t)

#x and y change for first pendelum
x1 = L1 * sin(y[:,0])
y1 = L1 * cos(y[:,0])

#second pendelum
x2 = L2 * sin(y[:,2]) + x1
y2 = L2 * cos(y[:,2]) + y1

fig = plt.figure()
ax = fig.add_subplot(111, autoscale_on = False, xlim = (-(L1+L2), L1+L2), ylim = (-(L1+L2), L1+L2))

ax.set_aspect("equal")
ax.grid()

line, = ax.plot([], [], "o-", lw = 2)
time_template = "time = %.2fs"
time_text = ax.text(0.04, 0.9, "", transform = ax.transAxes)

def init():
    line.set_data([], [])
    time_text.set_text("")
    return line, time_text

def animate(i):
    thisx = [0, x1[i], x2[i]]
    thisy = [0, y1[i], y2[i]]
    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i * dt))
    return line, time_text

ani = animation.FuncAnimation(fig, animate, range(1,len(y)), interval = dt * 1000, blit = True, init_func=init)
plt.show()
