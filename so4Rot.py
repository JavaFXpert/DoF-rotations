import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

theta = Parameter('theta')

crx = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, quil_cos(theta / 2), -1 * quil_sin(theta / 2)], [0, 0, quil_sin(theta / 2), quil_cos(theta / 2)]])
acrx = np.array([[quil_cos(theta / 2), -1 * quil_sin(theta / 2), 0, 0], [quil_sin(theta / 2), quil_cos(theta / 2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

dg_crx = DefGate('CRX', crx, [theta])
dg_acrx = DefGate('ACRX', acrx, [theta])

CRX = dg_crx.get_constructor()
ACRX = dg_acrx.get_constructor()

qvm = api.QVMConnection()
p = pq.Program()

p.inst(dg_crx)
p.inst(dg_acrx)

#p.inst(X(0))
#p.inst(X(1))

# CD rotation
p.inst(ACRX(np.pi/4)(1, 0))

# CE rotation
p.inst(ACRX(np.pi/4)(0, 1))

# CF rotation
p.inst(CNOT(0, 1))
p.inst(ACRX(np.pi/4)(1, 0))
p.inst(CNOT(0, 1))

# DE rotation
p.inst(CNOT(0, 1))
p.inst(CRX(np.pi/4)(1, 0))
p.inst(CNOT(0, 1))

# DF rotation
p.inst(CRX(np.pi/4)(0, 1))

# EF rotation
p.inst(CRX(np.pi/4)(1, 0))



wavefunction = qvm.wavefunction(p)
print(wavefunction)





