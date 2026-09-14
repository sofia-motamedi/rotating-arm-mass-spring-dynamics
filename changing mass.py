import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def f(t, y, m, k, l0, Omega, g):
    r, v = y
    drdt = v
    dvdt = r * Omega**2 - (k/m) * (r - l0) + g * np.cos(Omega * t)
    return np.array([drdt, dvdt])

# System parameters
m = 2.0        # mass in kg
k = 10.0       # spring constant in N/m
l0 = 0.5       # natural length in m
Omega = 1.0    # angular velocity in rad/s
g = 9.81       # gravitational acceleration in m/s^2

# Initial conditions
r0 = 0.4
v0 = 0.1
y0 = np.array([r0, v0])

# Time settings
ti = 0.0
tf = 30.0
dt = 0.01
t_values = np.arange(ti, tf + dt, dt)
N = len(t_values)

# Initialize an array to store the solution
y = np.zeros((N, 2))
y[0] = y0

# Runge-Kutta 4th order method (RK4)
for i in range(N - 1):
    t_current = t_values[i]
    y_current = y[i]
    
    k1 = f(t_current, y_current, m, k, l0, Omega, g)
    k2 = f(t_current + dt/2, y_current + (dt/2) * k1, m, k, l0, Omega, g)
    k3 = f(t_current + dt/2, y_current + (dt/2) * k2, m, k, l0, Omega, g)
    k4 = f(t_current + dt, y_current + dt * k3, m, k, l0, Omega, g)
    
    y[i + 1] = y_current + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

# Extract the radial position and velocity
r_values = y[:, 0]
v_values = y[:, 1]

theta = Omega * t_values              
x_values = r_values * np.sin(theta)    
y_values = -r_values * np.cos(theta)   

# Calculate the total Energy
E = 0.5 * m * (v_values**2 + (r_values * Omega)**2) + 0.5 * k * (r_values - l0)**2 + m * g * y_values

# Plot r(t)
plt.figure(figsize=(8, 4))
plt.plot(t_values, r_values)
plt.xlabel("Time (s)")
plt.ylabel("Radial position r (m)")
plt.title("RK4 solution: r(t)")
plt.grid(True)
plt.show()

# Plot r_dot(t)
plt.figure(figsize=(8, 4))
plt.plot(t_values, v_values, color="orange")
plt.xlabel("Time (s)")
plt.ylabel("Radial velocity r_dot (m/s)")
plt.title("RK4 solution: r_dot(t)")
plt.grid(True)
plt.show()

# Plot Energy versus Time
plt.figure(figsize=(10, 5))
plt.plot(t_values, E, color="purple")
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.title("E(t)")
plt.grid(True)
plt.show()

# Create a 3D plot where the horizontal axes are x and y, and the vertical axis is time
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x_values, y_values, t_values, color="b")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("Time (s)")
ax.set_title("Trajectory of mass")
plt.show()

#Set up the animated 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("Time (s)")
ax.set_title("Animated 3D Trajectory")
line, = ax.plot([], [], [], lw=2, label="Trajectory")
point, = ax.plot([], [], [], 'ro', markersize=5, label="Mass")
ax.set_xlim(np.min(x_values) - 0.1, np.max(x_values) + 0.1)
ax.set_ylim(np.min(y_values) - 0.1, np.max(y_values) + 0.1)
ax.set_zlim(t_values[0], t_values[-1])
def init_anim():
    line.set_data([], [])
    line.set_3d_properties([])
    point.set_data([], [])
    point.set_3d_properties([])
    return line, point
def update_anim(i):
    line.set_data(x_values[:i], y_values[:i])
    line.set_3d_properties(t_values[:i])
    point.set_data([x_values[i]], [y_values[i]])
    point.set_3d_properties([t_values[i]])
    return line, point
anim = FuncAnimation(fig, update_anim, frames=N, init_func=init_anim, interval=20, blit=False)
plt.legend()
plt.show()
anim.save("C:/Users/smota/OneDrive/Desktop/animation3.gif", writer="pillow")