# Mass–Spring System on a Rotating Arm


## 1. Physical problem: Mass–spring system on a rotating arm

This problem combines rotational motion and linear oscillation, which can lead to interesting dynamical behavior.  
We consider a point mass attached to a spring, moving along a rotating rigid arm (similar to the arm of a carousel).

### 1.1 System structure

- Rigid arm:
  - A massless rigid rod of length $L$, attached to a fixed point (center of rotation).
  - The rod rotates in a horizontal plane with constant angular velocity $\Omega$.

- Mass:
  - A point mass $m$ that can slide along the rod.

- Spring:
  - A linear spring with stiffness $k$ and natural length $L_0$.
  - One end of the spring is attached to the center of rotation, the other end to the mass $m$.

- Friction:
  - There is no friction between the mass and the rod.

---

## 2. Lagrangian formulation

### 2.1 Generalized coordinates

The most suitable generalized coordinates for this system are:

- $r$: radial distance of the mass from the center of rotation (position of the mass along the rod).
- $\theta$: angle that the arm makes with the vertical downward direction.

Since the arm rotates with constant angular velocity $\Omega$, we have:
$$\theta(t) = \Omega t$$

### 2.2 Cartesian coordinates of the mass

We consider motion in a vertical plane, with the vertical axis $y$ positive upwards.  
When $\theta = 0$, the arm is vertical and pointing downward, so the mass lies on the negative $y$-axis.

The Cartesian coordinates are:

$$x(t) = r \sin(\theta) = r \sin(\Omega t)$$

$$y(t) = -r \cos(\theta) = -r \cos(\Omega t)$$


---

### 2.3 Kinetic energy $T$

We first compute the velocity components by differentiating $x(t)$ and $y(t)$:

$$\dot{x} = \frac{d}{dt}[r \cos(\Omega t)] = \dot{r} \cos(\Omega t) - r \Omega \sin(\Omega t)$$
$$\dot{y} = \frac{d}{dt}[r \sin(\Omega t)] = -\dot{r} \sin(\Omega t) + r \Omega \cos(\Omega t)$$

Then:
$$\dot{x}^2 + \dot{y}^2 = \dot{r}^2 + r^2 \Omega^2$$

So the kinetic energy of the mass is:
$$T = \frac{1}{2} m \left( \dot{r}^2 + r^2 \Omega^2 \right)$$

---

### 2.4 Potential energy $V$

There are two sources of potential energy:

1. Spring potential:
   $$V_{\text{spring}} = \frac{1}{2} k (r - L_0)^2$$

2. Gravitational potential:

   Since the vertical position is $y = -r \cos(\Omega t)$ and $V_g = m g y$ with $y$ positive upwards:
   $$V_{\text{gravity}} = m g y = -m g r \cos(\Omega t)$$

Total potential energy:
$$V = V_{\text{spring}} + V_{\text{gravity}} = \frac{1}{2} k (r - L_0)^2 - m g r \cos(\Omega t)$$

---

### 2.5 Lagrangian $L$

The Lagrangian is:
$$L = T - V$$
$$L = \frac{1}{2} m \left( \dot{r}^2 + r^2 \Omega^2 \right) - \frac{1}{2} k (r - L_0)^2 + m g r \cos(\Omega t)$$

---

### 2.6 Euler–Lagrange equation

For the generalized coordinate $r$, the Euler–Lagrange equation is:
$$\frac{d}{dt} \left( \frac{\partial L}{\partial \dot{r}} \right) - \frac{\partial L}{\partial r} = 0$$

1. Derivative with respect to $\dot{r}$:
   $$\frac{\partial L}{\partial \dot{r}} = m \dot{r} \quad \Rightarrow \quad \frac{d}{dt} \left( m \dot{r} \right) = m \ddot{r}$$

2. Derivative with respect to $r$:

   - From the kinetic term:
     $$\frac{\partial}{\partial r} \left( \frac{1}{2} m r^2 \Omega^2 \right) = m r \Omega^2$$
   - From the spring term:
     $$\frac{\partial}{\partial r} \left( -\frac{1}{2} k (r - L_0)^2 \right) = -k (r - L_0)$$
   - From gravity:
     $$\frac{\partial}{\partial r} \left( m g r \cos(\Omega t) \right) = m g \cos(\Omega t)$$

   Thus:
   $$\frac{\partial L}{\partial r} = m r \Omega^2 - k (r - L_0) + m g \cos(\Omega t)$$

Putting into Euler–Lagrange:
$$m \ddot{r} - \left[ m r \Omega^2 - k (r - L_0) + m g \cos(\Omega t) \right] = 0$$
So the equation of motion is:
$$\ddot{r} = r \Omega^2 - \frac{k}{m} (r - L_0) + g \cos(\Omega t)$$


Note: $\theta(t) = \Omega t$ is prescribed by an external motor, so we do not derive a separate dynamical equation for $\theta$.

---

## 3. Conversion to a first-order system

To solve numerically, we convert the second-order ODE into a system of first-order ODEs.

Define:
- $x_1 = r$
- $x_2 = \dot{r}$

Then:
$$\dot{x}_1 = x_2$$
$$\dot{x}_2 = x_1 \Omega^2 - \frac{k}{m} (x_1 - L_0) + g \cos(\Omega t)$$

So the system is:
$$\frac{dx_1}{dt} = x_2$$
$$\frac{dx_2}{dt} = x_1 \Omega^2 - \frac{k}{m} (x_1 - L_0) + g \cos(\Omega t)$$

---

## 4. Numerical implementation in Python

We use numerical integration (Runge–Kutta 4th order, RK4) to solve the system over a time interval, e.g. $t \in [0, 30]$ s, with sufficiently small time steps.

### 4.1 System parameters

We consider and compare different parameter sets:

- Mass $m$:
  - $m = 1\ \text{kg}$
  - $m = 2\ \text{kg}$

- Spring constant $k$:
  - $k = 10\ \text{N/m}$
  - $k = 15\ \text{N/m}$

- Natural length $L_0$:
  - $L_0 = 0.5\ \text{m}$
  - $L_0 = 0.7\ \text{m}$

- Angular velocity $\Omega$:
  - $\Omega = 1\ \text{rad/s}$
  - $\Omega = 1.5\ \text{rad/s}$

### 4.2 Initial conditions

We test different initial conditions:

1. $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$
2. $r(0) = 0.6\ \text{m},\ \dot{r}(0) = 0\ \text{m/s}$

---

## 5. Euler vs RK4 (accuracy discussion)

Euler’s method is a first-order method that approximates the change in state linearly at each time step.  
RK4 uses multiple intermediate evaluations ($k_1, k_2, k_3, k_4$) and achieves much higher accuracy.

For a given time step size:

- Euler method:
  - Lower accuracy.
  - Error accumulates over time, especially in sensitive dynamical systems (like this one with centrifugal and gravitational forces).
  - Even with small $\Delta t$, accumulated error can significantly distort the trajectory.

- RK4 method:
  - Much more accurate for the same $\Delta t$.
  - Better preserves the qualitative behavior of the system over long integration times.

Therefore, Euler’s method is not suitable for this problem; RK4 is preferred.

---

## 6. Trajectory of the mass in the XY plane

Using the numerical solution $r(t)$ and $\theta(t) = \Omega t$, we compute:
$$x(t) = r(t) \sin(\Omega t), \quad y(t) = -r(t) \cos(\Omega t)$$
and plot the trajectory in the $XY$-plane.

Below are the figures corresponding to different parameter sets and initial conditions.  
(Replace the file paths with your actual image and video files.)

### 6.1 Case 1: Baseline parameters

- $m = 1\ \text{kg}$
- $k = 10\ \text{N/m}$
- $L_0 = 0.5\ \text{m}$
- $\Omega = 1\ \text{rad/s}$
- $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$

#### Trajectory figure

<img src="figures/Initial conditions (trajectory of mass).png" alt="Initial conditions trajectory of mass" />

#### Trajectory video (MP4)

[Trajectory of mass — baseline (MP4)](videos/trajectory_m1_k10_L0.5_O1_r0_0.4_v0_0.1.mp4)

---

### 6.2 Case 2: Different initial conditions

- $m = 1\ \text{kg}$
- $k = 10\ \text{N/m}$
- $L_0 = 0.5\ \text{m}$
- $\Omega = 1\ \text{rad/s}$
- $r(0) = 0.6\ \text{m},\ \dot{r}(0) = 0\ \text{m/s}$

![Trajectory of mass — changed initial conditions](figures/trajectory_m1_k10_L0.5_O1_r0_0.6_v0_0.0.png)

[Trajectory of mass — changed initial conditions (MP4)](videos/trajectory_m1_k10_L0.5_O1_r0_0.6_v0_0.0.mp4)

---

### 6.3 Case 3: Increased mass

- $m = 2\ \text{kg}$
- $k = 10\ \text{N/m}$
- $L_0 = 0.5\ \text{m}$
- $\Omega = 1\ \text{rad/s}$
- $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$

![Trajectory of mass — increased mass](figures/trajectory_m2_k10_L0.5_O1_r0_0.4_v0_0.1.png)

[Trajectory of mass — increased mass (MP4)](videos/trajectory_m2_k10_L0.5_O1_r0_0.4_v0_0.1.mp4)

Qualitative effects of increasing mass:
- Increased inertia: The mass resists changes in motion more strongly.
- Reduced radial oscillation amplitude: Since the restoring acceleration is $-\frac{k}{m}(r - L_0)$, larger $m$ reduces acceleration, so $r(t)$ varies less.
- Lower natural frequency: $\omega_{\text{nat}} = \sqrt{k/m}$ decreases with increasing $m$, so oscillations are slower.
- Smoother trajectory: The path in the $XY$-plane appears smoother and less oscillatory.

---

### 6.4 Case 4: Increased spring constant

- $m = 1\ \text{kg}$
- $k = 15\ \text{N/m}$
- $L_0 = 0.5\ \text{m}$
- $\Omega = 1\ \text{rad/s}$
- $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$

![Trajectory of mass — increased spring constant](figures/trajectory_m1_k15_L0.5_O1_r0_0.4_v0_0.1.png)

[Trajectory of mass — increased spring constant (MP4)](videos/trajectory_m1_k15_L0.5_O1_r0_0.4_v0_0.1.mp4)

Effects of increasing $k$:

- Stiffer system: Stronger restoring force for radial deviations.
- Smaller radial oscillation amplitude: $r(t)$ stays closer to $L_0$.
- Higher natural frequency: $\omega_{\text{nat}} = \sqrt{k/m}$ increases, so oscillations are faster.
- Trajectory: Small, rapid oscillations around a nearly circular path.

---

### 6.5 Case 5: Increased natural length $L_0$

- $m = 1\ \text{kg}$
- $k = 10\ \text{N/m}$
- $L_0 = 0.7\ \text{m}$
- $\Omega = 1\ \text{rad/s}$
- $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$

![Trajectory of mass — increased natural length](figures/trajectory_m1_k10_L0.7_O1_r0_0.4_v0_0.1.png)

[Trajectory of mass — increased natural length (MP4)](videos/trajectory_m1_k10_L0.7_O1_r0_0.4_v0_0.1.mp4)

Effects of increasing $L_0$:

- Shift of equilibrium radius: The equilibrium point moves outward.
- Higher mean radius: $r(t)$ oscillates around a larger average value.
- Trajectory: The mass moves on a path farther from the center.

---

### 6.6 Case 6: Increased angular velocity $\Omega$

- $m = 1\ \text{kg}$
- $k = 10\ \text{N/m}$
- $L_0 = 0.5\ \text{m}$
- $\Omega = 1.5\ \text{rad/s}$
- $r(0) = 0.4\ \text{m},\ \dot{r}(0) = 0.1\ \text{m/s}$

![Trajectory of mass — increased angular velocity](figures/trajectory_m1_k10_L0.5_O1.5_r0_0.4_v0_0.1.png)

[Trajectory of mass — increased angular velocity (MP4)](videos/trajectory_m1_k10_L0.5_O1.5_r0_0.4_v0_0.1.mp4)

Effects of increasing $\Omega$:

- Stronger centrifugal term $r \Omega^2$: Pushes the mass outward, increasing the equilibrium radius.
- Faster rotation: The mass completes more revolutions in the same time interval.
- Modified radial dynamics: Competition between centrifugal force and spring force can change amplitude and pattern of radial oscillations.
- Trajectory: More tightly wound, rapidly rotating path with outward shift.

---

## 7. Radial position and velocity vs time

For each case, we also plot:

- Radial position: $r(t)$
- Radial velocity: $\dot{r}(t)$

Again, replace the file paths with your actual figures.

### 7.1 Baseline case

- $m = 1\ \text{kg}, k = 10\ \text{N/m}, L_0 = 0.5\ \text{m}, \Omega = 1\ \text{rad/s}$
- $r(0) = 0.4\ \text{m}, \dot{r}(0) = 0.1\ \text{m/s}$

![RK4 solution: r(t) — baseline](figures/r_t_m1_k10_L0.5_O1_r0_0.4_v0_0.1.png)
![RK4 solution: r_dot(t) — baseline](figures/rdot_t_m1_k10_L0.5_O1_r0_0.4_v0_0.1.png)

---

### 7.2 Changed initial conditions

![RK4 solution: r(t) — changed IC](figures/r_t_m1_k10_L0.5_O1_r0_0.6_v0_0.0.png)
![RK4 solution: r_dot(t) — changed IC](figures/rdot_t_m1_k10_L0.5_O1_r0_0.6_v0_0.0.png)

---

### 7.3 Increased mass

![RK4 solution: r(t) — increased mass](figures/r_t_m2_k10_L0.5_O1_r0_0.4_v0_0.1.png)
![RK4 solution: r_dot(t) — increased mass](figures/rdot_t_m2_k10_L0.5_O1_r0_0.4_v0_0.1.png)

Summary of mass effects on $r(t)$ and $\dot{r}(t)$:

- Lower natural frequency.
- Slower response (gentler slopes in $r(t)$).
- Slower oscillations in $\dot{r}(t)$.

---

### 7.4 Increased spring constant
![RK4 solution: r(t) — increased k](figures/r_t_m1_k15_L0.5_O1_r0_0.4_v0_0.1.png)
![RK4 solution: r_dot(t) — increased k](figures/rdot_t_m1_k15_L0.5_O1_r0_0.4_v0_0.1.png)

Summary of $k$ effects:

- Higher natural frequency.
- Smaller amplitude of $r(t)$ oscillations.
- Faster oscillations in $\dot{r}(t)$.

---

### 7.5 Increased natural length $L_0$

![RK4 solution: r(t) — increased L0](figures/r_t_m1_k10_L0.7_O1_r0_0.4_v0_0.1.png)
![RK4 solution: r_dot(t) — increased L0](figures/rdot_t_m1_k10_L0.7_O1_r0_0.4_v0_0.1.png)

Summary of $L_0$ effects:

- Shift of equilibrium radius outward.
- $r(t)$ oscillates around a larger mean value.
- $\dot{r}(t)$ pattern largely unchanged except for small amplitude changes.

---

### 7.6 Increased angular velocity $\Omega$

![RK4 solution: r(t) — increased Omega](figures/r_t_m1_k10_L0.5_O1.5_r0_0.4_v0_0.1.png)
![RK4 solution: r_dot(t) — increased Omega](figures/rdot_t_m1_k10_L0.5_O1.5_r0_0.4_v0_0.1.png)

Summary of $\Omega$ effects:

- Outward shift of equilibrium radius due to stronger centrifugal force.
- Faster temporal variation of gravitational term $\cos(\Omega t)$.
- Shorter oscillation periods in both $r(t)$ and $\dot{r}(t)$.

---

## 8. Energy analysis

We define the mechanical energy associated with radial motion and spring/gravity:

$$E(t) = \frac{1}{2} m \dot{r}(t)^2 + \frac{1}{2} m r(t)^2 \Omega^2 + \frac{1}{2} k (r(t) - L_0)^2 - m g r(t) \cos(\Omega t)$$

Note: Because the rod is driven at constant angular velocity by an external motor, the total mechanical energy of the full system (including the rotating arm) is not conserved. However, the energy associated with radial motion and the spring potential still provides useful information about the dynamics.

### 8.1 Baseline case

![Energy E(t) — baseline](figures/E_t_m1_k10_L0.5_O1_r0_0.4_v0_0.1.png)

---

### 8.2 Changed initial conditions

![Energy E(t) — changed IC](figures/E_t_m1_k10_L0.5_O1_r0_0.6_v0_0.0.png)

---

### 8.3 Increased mass

![Energy E(t) — increased mass](figures/E_t_m2_k10_L0.5_O1_r0_0.4_v0_0.1.png)

Effects of increasing mass on energy:

- Higher overall energy level: Kinetic and gravitational terms scale with $m$.
- Slower energy oscillations: Due to reduced natural frequency and increased inertia, energy exchange between kinetic and potential components occurs more slowly.

---

### 8.4 Increased spring constant

![Energy E(t) — increased k](figures/E_t_m1_k15_L0.5_O1_r0_0.4_v0_0.1.png)

Effects of increasing $k$:

- Greater sensitivity of potential energy to displacement: Since $V_{\text{spring}} = \frac{1}{2} k (r - L_0)^2$, larger $k$ increases energy for a given displacement.
- Faster oscillations in energy: Higher natural frequency leads to more rapid energy exchange between kinetic and potential parts.

---

## 9. How to run the simulation (example)

Below is an example structure for the Python code (you can adapt it to your actual implementation):

`python
import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0      # kg
k = 10.0     # N/m
L0 = 0.5     # m
Omega = 1.0  # rad/s
g = 9.81     # m/s^2

# Time settings
t0, t_end = 0.0, 30.0
dt = 0.001
t = np.arange(t0, t_end + dt, dt)

# Initial conditions
r0 = 0.4     # m
rdot0 = 0.1  # m/s

def f(t, x1, x2):
    """Right-hand side of the first-order system."""
    dx1dt = x2
    dx2dt = x1 * Omega**2 - (k/m) * (x1 - L0) + g * np.cos(Omega * t)
    return dx1dt, dx2dt

def rk4_step(t, x1, x2, dt):
    k1_1, k1_2 = f(t, x1, x2)
    k2_1, k2_2 = f(t + dt/2, x1 + dt*k1_1/2, x2 + dt*k1_2/2)
    k3_1, k3_2 = f(t + dt/2, x1 + dt*k2_1/2, x2 + dt*k2_2/2)
    k4_1, k4_2 = f(t + dt, x1 + dt*k3_1, x2 + dt*k3_2)

    x1_new = x1 + dt * (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6
    x2_new = x2 + dt * (k1_2 + 2*k2_2 + 2*k3_2 + k4_2) / 6
    return x1_new, x2_new

# Integration
r = np.zeros_like(t)
rdot = np.zeros_like(t)
r[0], rdot[0] = r0, rdot0

for i in range(len(t) - 1):
    r[i+1], rdot[i+1] = rk4_step(t[i], r[i], rdot[i], dt)

# Compute x, y
theta = Omega * t
x = r * np.sin(theta)
y = -r * np.cos(theta)
# Plot trajectory
plt.figure()
plt.plot(x, y)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Trajectory of mass')
plt.axis('equal')
plt.grid(True)
plt.savefig('figures/trajectory_m1_k10_L0.5_O1_r0_0.4_v0_0.1.png', dpi=300)
plt.show()
