# Mass-Spring System on a Rotating Arm

Author: Sofia Motamedilamouki, B.Sc. Physics, Amirkabir University of Technology[span_0](start_span)[span_0](end_span)

## Overview
This project explores the physical dynamics of a mass-spring system connected to a rotating arm, similar to a Ferris wheel mechanism[span_1](start_span)[span_1](end_span). The combination of linear oscillation and rotational motion produces complex dynamical behaviors driven by restoring spring forces, gravity, and centrifugal effects[span_2](start_span)[span_2](end_span).

### System Architecture
* A massless rigid arm of length $L$ rotates at a constant angular velocity $\Omega$ in the horizontal plane around a fixed center point[span_3](start_span)[span_3](end_span).
* A point mass $m$ slides without friction along this arm[span_4](start_span)[span_4](end_span).
* A spring with spring constant $k$ and natural length $l_0$ connects the mass to the center of rotation[span_5](start_span)[span_5](end_span).

## Lagrangian Formulation

### Generalized Coordinates
The system is defined by two generalized coordinates based on its geometry[span_6](start_span)[span_6](end_span):
1. $r$: The radial distance of the mass from the center of rotation[span_7](start_span)[span_7](end_span).
2. $\theta$: The angle the arm makes with the downward vertical axis[span_8](start_span)[span_8](end_span). 

Because the arm rotates at a constant angular velocity, the angle is a known function of time: $\theta(t) = \Omega t$[span_9](start_span)[span_9](end_span). 

In Cartesian coordinates (where the positive y-axis points upwards and $\theta = 0$ is completely vertical downwards), the position of the mass is[span_10](start_span)[span_10](end_span):
$$x = r\sin(\Omega t)$$
$$y = -r\cos(\Omega t)$$

### Kinetic and Potential Energy
Taking the time derivatives of $x$ and $y$ yields the velocity components[span_11](start_span)[span_11](end_span):
$$\dot{x} = \dot{r}\sin(\Omega t) + r\Omega\cos(\Omega t)$$
$$\dot{y} = -\dot{r}\cos(\Omega t) + r\Omega\sin(\Omega t)$$

Squaring and summing these components gives $\dot{x}^2 + \dot{y}^2 = \dot{r}^2 + r^2\Omega^2$, allowing us to write the kinetic energy ($T$) as[span_12](start_span)[span_12](end_span):
$$T = \frac{1}{2}m(\dot{r}^2 + r^2\Omega^2)$$

The total potential energy ($V$) comes from two sources—the elastic energy of the spring and gravity[span_13](start_span)[span_13](end_span):
$$V_{spring} = \frac{1}{2}k(r - l_0)^2$$
$$V_{gravity} = mgy = -mgr\cos(\Omega t)$$
$$V = \frac{1}{2}k(r - l_0)^2 - mgr\cos(\Omega t)$$

### Euler-Lagrange Equation
The Lagrangian is $L = T - V$[span_14](start_span)[span_14](end_span):
$$L = \frac{1}{2}m(\dot{r}^2 + r^2\Omega^2) - \frac{1}{2}k(r - l_0)^2 + mgr\cos(\Omega t)$$

Applying the Euler-Lagrange equation for the radial coordinate $r$[span_15](start_span)[span_15](end_span):
$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{r}}\right) - \frac{\partial L}{\partial r} = 0$$

* Time derivative term: $\frac{\partial L}{\partial \dot{r}} = m\dot{r} \Rightarrow \frac{d}{dt}(m\dot{r}) = m\ddot{r}$[span_16](start_span)[span_16](end_span).
* Radial derivative term: $\frac{\partial L}{\partial r} = mr\Omega^2 - k(r - l_0) + mg\cos(\Omega t)$[span_17](start_span)[span_17](end_span).

Setting these equal gives the final second-order differential equation of motion[span_18](start_span)[span_18](end_span):
$$\ddot{r} = r\Omega^2 - \frac{k}{m}(r - l_0) + g\cos(\Omega t)$$

## Numerical Implementation
Because $\theta(t)$ is driven by external forces (e.g., a motor) and is a known function of time, it does not require a separate dynamical equation[span_19](start_span)[span_19](end_span). To solve the radial equation of motion, the second-order differential equation is converted into a system of first-order equations by defining $x_1 = r$ and $x_2 = \dot{r}$[span_20](start_span)[span_20](end_span):
$$\dot{x}_1 = x_2$$
$$\dot{x}_2 = x_1\Omega^2 - \frac{k}{m}(x_1 - l_0) + g\cos(\Omega t)$$
Integrator Choice (RK4 vs. Euler):
This system is evaluated over a 30-second timeframe using a 4th-Order Runge-Kutta (RK4) method rather than a first-order Euler method[span_21](start_span)[span_21](end_span). Euler methods utilize a linear approximation for each time step[span_22](start_span)[span_22](end_span). In dynamical systems highly sensitive to centrifugal and gravitational forces, the error from Euler integration accumulates over time, fundamentally altering the shape of the resulting trajectory[span_23](start_span)[span_23](end_span). RK4 mitigates this by calculating multiple intermediate estimations ($k_1, k_2, k_3, k_4$) per step, providing the accuracy required for long-duration oscillation modeling[span_24](start_span)[span_24](end_span).

## Simulation Results and Analysis

### 1. Baseline System Trajectory
Parameters: $m = 1 \text{ kg}$, $k = 10 \text{ N/m}$, $l_0 = 0.5 \text{ m}$, $\Omega = 1 \text{ rad/s}$ | Initial Conditions: $r(0) = 0.4 \text{ m}$, $\dot{r}(0) = 0.1 \text{ m/s}$[span_25](start_span)[span_25](end_span)[span_26](start_span)[span_26](end_span).
![Baseline Static Plot](diagram1.png) 
![Baseline Animation](animation1.gif)

### 2. Modified Initial Conditions
Parameters: $m = 1 \text{ kg}$, $k = 10 \text{ N/m}$, $l_0 = 0.5 \text{ m}$, $\Omega = 1 \text{ rad/s}$ | Initial Conditions: $r(0) = 0.6 \text{ m}$, $\dot{r}(0) = 0 \text{ m/s}$[span_27](start_span)[span_27](end_span)[span_28](start_span)[span_28](end_span).
![Modified IC Static Plot](diagram2.png) 
![Modified IC Animation](animation2.gif)

### 3. Impact of Increased Mass
Parameters: $m = 2 \text{ kg}$, $k = 10 \text{ N/m}$, $l_0 = 0.5 \text{ m}$, $\Omega = 1 \text{ rad/s}$ | Initial Conditions: $r(0) = 0.4 \text{ m}$, $\dot{r}(0) = 0.1 \text{ m/s}$[span_29](start_span)[span_29](end_span)[span_30](start_span)[span_30](end_span).
![Increased Mass Static Plot](diagram3.png) 
![Increased Mass Animation](animation3.gif)

Physical Analysis:
Increasing the mass to 2 kg increases the inertia of the system, meaning the mass exhibits greater resistance to changes in its state[span_31](start_span)[span_31](end_span). 
* Decreased Radial Amplitude: The acceleration caused by the spring's restoring force is proportional to $\frac{1}{m}$[span_32](start_span)[span_32](end_span). A larger mass reduces this acceleration, constraining the variance of $r(t)$ and resulting in a smoother, more uniform trajectory[span_33](start_span)[span_33](end_span).
* Decreased Oscillation Frequency: The natural frequency of the spring-mass system is $\omega = \sqrt{\frac{k}{m}}$[span_34](start_span)[span_34](end_span). Increasing the mass consequently lowers the frequency of the radial oscillations[span_35](start_span)[span_35](end_span).

### 4. Additional Parameter Explorations
* Increased Angular Velocity ($\Omega = 1.5 \text{ rad/s}$):[span_36](start_span)[span_36](end_span)
  ![Increased Omega](animation6.gif)
* Increased Spring Constant ($k = 15 \text{ N/m}$):[span_37](start_span)[span_37](end_span)
  ![Increased Spring Constant](animation4.gif)
* Increased Natural Length ($l_0 = 0.7 \text{ m}$):[span_38](start_span)[span_38](end_span)
  ![Increased Length](animation5.gif)
