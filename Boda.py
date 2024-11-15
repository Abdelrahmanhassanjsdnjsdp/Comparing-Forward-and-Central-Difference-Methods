import numpy 
import rebound
sim = rebound.Simulation()
sim.G = 1
sim.start_server(1111)
sim.add(m=1, r=1)                 
sim.add(m=0.001, r=0.1, a=2)         
sim.dt = 0.00050
for i in range(1000000):  
    sim.integrate(sim.t + sim.dt)
