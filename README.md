\frac{\partial\mathcal{L}}{\partial r}
=
mr\Omega^2-k(r-l_0)+mg\cos(\Omega t).
\]",
    r"Also,

\[
\frac{\partial\mathcal{L}}{\partial r}
=
mr\Omega^2-k(r-l_0)+mg\cos(\Omega t).
\]"
)

# Write Markdown through pypandoc as requested for generated .md files.
pypandoc.convert_text(
    readme,
    "md",
    format="md",
    outputfile=str(base / "README.md"),
    extra_args=["--standalone"],
)

# Copy the extracted figures with the repository-friendly names.
source_assets = Path("/mnt/data/github_assets")
for item in source_assets.iterdir():
    shutil.copy2(item, fig_dir / item.name)

# Preserve the original uploaded report in docs/.
shutil.copy2(
    "/mnt/data/پروژه درس محاسبات عددی.pdf",
    docs_dir / "numerical_computations_project.pdf"
)

# Put the reconstructed runnable code in src/.
code = r'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


def f(t, y, m, k, l0, Omega, g):
    r, v = y
    drdt = v
    dvdt = r * Omega**2 - (k / m) * (r - l0) + g * np.cos(Omega * t)
    return np.array([drdt, dvdt])


# System parameters
m = 1.0
k = 10.0
l0 = 0.5
Omega = 1.0
g = 9.81

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

# Initialize solution array
y = np.zeros((N, 2))
y[0] = y0

# Runge-Kutta 4th order method (RK4)
for i in range(N - 1):
    t_current = t_values[i]
    y_current = y[i]

    k1 = f(t_current, y_current, m, k, l0, Omega, g)
    k2 = f(
        t_current + dt / 2,
        y_current + (dt / 2) * k1,
        m, k, l0, Omega, g
    )
    k3 = f(
        t_current + dt / 2,
        y_current + (dt / 2) * k2,
        m, k, l0, Omega, g
    )
    k4 = f(
        t_current + dt,
        y_current + dt * k3,
        m, k, l0, Omega, g
    )

    y[i + 1] = y_current + (dt / 6) * (
        k1 + 2 * k2 + 2 * k3 + k4
    )

# Extract radial position and velocity
r_values = y[:, 0]
v_values = y[:, 1]

# Convert to Cartesian coordinates
theta = Omega * t_values
x_values = r_values * np.sin(theta)
y_values = -r_values * np.cos(theta)

# Calculate total energy
E = (
    0.5 * m * (v_values2 + (r_values * Omega)2)
    + 0.5 * k * (r_values - l0)**2
    + m * g * y_values
)

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
plt.plot(t_values, v_values)
plt.xlabel("Time (s)")
plt.ylabel("Radial velocity r_dot (m/s)")
plt.title("RK4 solution: r_dot(t)")
plt.grid(True)
plt.show()

# Plot energy versus time
plt.figure(figsize=(10, 5))
plt.plot(t_values, E)
plt.xlabel("Time (s)")
plt.ylabel("Energy (J)")
plt.title("E(t)")
plt.grid(True)
plt.show()

# Create a 3D trajectory plot
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d")
ax.plot(x_values, y_values, t_values)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("Time (s)")
ax.set_title("Trajectory of mass")
plt.show()

# Set up animated 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_zlabel("Time (s)")
ax.set_title("Animated 3D Trajectory")

line, = ax.plot([], [], [], lw=2, label="Trajectory")
point, = ax.plot([], [], [], "ro", markersize=5, label="Mass")

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
    anim = FuncAnimation(
    fig,
    update_anim,
    frames=N,
    init_func=init_anim,
    interval=20,
    blit=False
)

plt.legend()
plt.show()

# Save the animation
anim.save("media/trajectory.gif", writer="pillow")
'''

(src_dir / "rotating_spring_mass.py").write_text(code, encoding="utf-8")

# Add a small placeholder README for the media folder explaining the MP4 must be supplied.
(media_dir / "README.md").write_text(
    "# Animation files\n\n"
    "Place the MP4 animation generated for this project here as trajectory.mp4.\n"
    "The PDF report references an animation as an attachment, but that MP4 file was not included in the uploaded PDF.\n",
    encoding="utf-8",
)

# Zip the ready-to-upload project bundle.
zip_path = Path("/mnt/data/rotating-spring-mass-github.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for path in base.rglob("*"):
        if path.is_file():
            z.write(path, path.relative_to(base.parent))

print(f"README created: {base / 'README.md'}")
print(f"GitHub project bundle created: {zip_path}")
print(f"Figures included: {len(list(fig_dir.iterdir()))}")
