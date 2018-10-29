import matplotlib.pyplot as plt
import numpy as np

fig = plt.gcf()
Energies = []
with open('IntegratedEnergies_nonlinear_30pc.txt') as data:	
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies.append(float(line)) 

NormalisedEnergies=[]
for i in range(0,len(Energies)):
	NormalisedEnergies.append(Energies[i]/Energies[0])
	print(NormalisedEnergies[i])
plt.plot(NormalisedEnergies,label = "n_p=0.1n_b")

Energies2 = []
with open('IntegratedEnergies_quasi_30pc.txt') as data:	
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies2.append(float(line)) 

NormalisedEnergies2=[]
for i in range(0,len(Energies2)):
	NormalisedEnergies2.append(Energies2[i]/Energies2[0])
	print(NormalisedEnergies2[i])
plt.plot(NormalisedEnergies2, label = "n_p=n_b")

Energies3 = []
with open('IntegratedEnergies_linear_30pc.txt') as data:    
    datalines = (line.rstrip('\r\n') for line in data)
    for line in datalines:
        Energies3.append(float(line)) 

NormalisedEnergies3=[]
for i in range(0,len(Energies3)):
    NormalisedEnergies3.append(Energies3[i]/Energies3[0])
    print(NormalisedEnergies3[i])
plt.plot(NormalisedEnergies3, label = "n_p=10n_b")

plt.legend(loc='best')


x = [0,85,170,255,340]
labels = ['0', '0.85', '1.70', '2,55', '3.40'] 
plt.xlabel('Propagation distance (cm)')
plt.ylabel('T/T$_0$')
plt.xticks(x, labels, rotation='horizontal')



plt.show()
fig.savefig('Energy30pc.pdf')