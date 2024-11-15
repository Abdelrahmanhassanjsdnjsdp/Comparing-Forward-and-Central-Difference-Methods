# Orbital Simulation with REBOUND

## Introduction
This script uses the **REBOUND** library to simulate a simple two-body orbital system. It demonstrates how to initialize a gravitational simulation, add celestial bodies, and perform numerical integration to track their motion over time.

---

## Requirements
To run this code, ensure you have the following libraries installed:

- **NumPy**: For numerical computations.
- **REBOUND**: A library for N-body simulations.

Install the dependencies using:
```bash
pip install numpy rebound
```

---

## Code Description

### 1. **Imports**
The script imports:
- `numpy`: General numerical operations.
- `rebound`: Core library for orbital mechanics.

### 2. **Simulation Initialization**
- A `rebound.Simulation` object is created.
- The gravitational constant (`G`) is set to 1 for normalized units.

### 3. **Server Setup**
The simulation starts a server on port `1111` using `sim.start_server(1111)`, allowing external tools to connect and visualize or interact with the simulation.

### 4. **Adding Bodies**
- **Central Body**: A massive central body (e.g., a star) is added with:
  - Mass: `m=1`
  - Radius: `r=1`
- **Orbiting Body**: A smaller body (e.g., a planet) is added with:
  - Mass: `m=0.001`
  - Radius: `r=0.1`
  - Semi-major axis: `a=2`

### 5. **Integration**
The simulation is run for 1,000,000 steps. During each step, the state of the system is updated by integrating forward in time using `sim.integrate(sim.t + sim.dt)`.

---

## Running the Code
1. Save the code to a file, e.g., `simulation.py`.
2. Run the script:
   ```bash
   python simulation.py
   ```

---

## Key Parameters
- **Gravitational Constant (`G`)**: Set to `1` for simplicity.
- **Bodies**:
  - Central body: `m=1`, `r=1`.
  - Orbiting body: `m=0.001`, `r=0.1`, `a=2`.
- **Time Step (`dt`)**: The integration time step is set to `0.00050`.

---

## Potential Enhancements
- **Visualization**: Incorporate visualization tools such as matplotlib or REBOUND's GUI for real-time tracking of orbits.
- **Data Logging**: Save positions and velocities of bodies for later analysis or plotting.
- **Multi-body Simulation**: Add more bodies to simulate complex gravitational interactions.
- **Adjustable Parameters**: Allow users to input or modify simulation parameters (e.g., masses, initial positions, and velocities).

---

## Notes
- The server functionality (`sim.start_server`) enables external connection but requires additional tools to visualize or interact with the simulation.
- Running 1,000,000 iterations can be computationally intensive. Consider optimizing the code for large-scale simulations.

---

## Resources
- [REBOUND Documentation](https://rebound.readthedocs.io/): Comprehensive guide to REBOUND features and usage.
- [NumPy Documentation](https://numpy.org/doc/): For numerical computations. 

