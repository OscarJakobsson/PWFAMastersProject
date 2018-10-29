import matplotlib.pyplot as plt
import numpy as np

fig = plt.gcf()
Energies = []
with open('IntegratedEnergies_nonlinear_30pc.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies.append(float(line)) 
Particles = []        
with open('IntegratedEnergies_nonlinear_30pc_particles.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Particles.append(float(line)) 
NormalisedEnergies=[]
for i in range(0,int((len(Energies)-1)/34)):
    NormalisedEnergies.append((Energies[i*34]/Particles[i]) / (Energies[0]/Particles[0]))
    #print(NormalisedEnergies[i])
plt.plot(NormalisedEnergies,label = "n_p=0.1n_b")

Energies2 = []
with open('IntegratedEnergies_quasi_30pc_past_sat_length.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies2.append(float(line)) 
Particles2 = []        
with open('IntegratedEnergies_quasi_30pc_particles_past_sat_length.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Particles2.append(float(line)) 
NormalisedEnergies2=[]
for i in range(0,int((len(Energies2)-1)/34)):
    NormalisedEnergies2.append((Energies2[i*34]/Particles2[i]) / (Energies2[0]/Particles2[0]))
    #print(NormalisedEnergies[i])
plt.plot(NormalisedEnergies2,label = "n_p=n_b")

Energies3 = []
with open('IntegratedEnergies_linear_30pc.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies3.append(float(line)) 
Particles3 = []        
with open('IntegratedEnergies_linear_30pc_particles.txt') as data: 
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Particles3.append(float(line)) 
NormalisedEnergies3=[]
for i in range(0,int((len(Energies3)-1)/34)):
    NormalisedEnergies3.append((Energies3[i*34]/Particles3[i]) / (Energies3[0]/Particles3[0]))
    #print(NormalisedEnergies3[i])
plt.plot(NormalisedEnergies3,label = "n_p=10n_b")

plt.legend(loc='best')


x = [0,2.25,4.5,6.85,9]
labels = ['0', '0.85', '1.70', '2,55', '3.40'] 
plt.xlabel('Propagation distance (cm)')
plt.ylabel('T/T$_0$  [per simulated particle]')
plt.xticks(x, labels, rotation='horizontal')



plt.show()
fig.savefig('Energy30pc_per_particle.pdf')