import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
G = 6.67430e-11  # Gravitational constant (m^3 kg^-1 s^-2)
time_step = 1e5  # Time step (s)
num_steps = 20000  # Number of simulation steps

# Star properties
star_mass = 2e30  # Mass of the star (kg)
star_position = np.array([0, 0])  # Fixed position of the star

# Planet properties (mass, initial position, initial velocity)
planets = [
    {"mass": 6e24, "position": np.array([1.5e11, 0]), "velocity": np.array([0, 3e4])},  # Earth-like
    {"mass": 3e24, "position": np.array([2.5e11, 0]), "velocity": np.array([0, 2.5e4])},  # Smaller
    {"mass": 9e24, "position": np.array([1e11, 0]), "velocity": np.array([0, 3.5e4])},  # Larger
]

# Store positions for plotting
positions = [np.zeros((num_steps, 2)) for _ in planets]

# Calculate gravitational force
def gravitational_force(m1, m2, r1, r2):
    r = r2 - r1
    distance = np.linalg.norm(r)
    force_magnitude = G * m1 * m2 / distance**2
    force_direction = r / distance
    return force_magnitude * force_direction

# Simulation
for step in range(num_steps):
    for i, planet in enumerate(planets):
        # Compute gravitational force with the star
        force = gravitational_force(planet["mass"], star_mass, planet["position"], star_position)

        # Update velocity and position (Velocity-Verlet)
        acceleration = force / planet["mass"]
        planet["velocity"] += acceleration * time_step
        planet["position"] += planet["velocity"] * time_step

        # Store position
        positions[i][step] = planet["position"]

# Visualization
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-3e11, 3e11)
ax.set_ylim(-3e11, 3e11)
ax.set_aspect('equal')

star = plt.plot(0, 0, 'yo', markersize=10, label="Star")[0]
planet_lines = [ax.plot([], [], '-', alpha=0.7)[0] for _ in planets]
planet_points = [ax.plot([], [], 'o')[0] for _ in planets]
colors = ['blue', 'red', 'green']

def update(frame):
    for i, line in enumerate(planet_lines):
        line.set_data(positions[i][:frame, 0], positions[i][:frame, 1])
        planet_points[i].set_data(positions[i][frame, 0], positions[i][frame, 1])
        planet_points[i].set_color(colors[i])
    return planet_lines + planet_points

ani = FuncAnimation(fig, update, frames=num_steps, interval=1, blit=True)
plt.legend()
plt.show()
