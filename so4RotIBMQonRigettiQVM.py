import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

qvm = api.QVMConnection()
p = pq.Program()

# p.inst(X(0))
# p.inst(X(1))

# CD rotation (GOOD)
# p.inst(X(1))
# p.inst(CNOT(1, 0))
# p.inst(RY(-1 * np.pi/8)(0))
# p.inst(CNOT(1, 0))
# p.inst(RY(np.pi/8)(0))
# p.inst(X(1))


# CE rotation (GOOD)
# p.inst(X(0))
# p.inst(H(0))
# p.inst(H(1))
# p.inst(CNOT(1, 0))
# p.inst(RY(np.pi/8)(1))
# p.inst(CNOT(1, 0))
# p.inst(H(0))
# p.inst(H(1))
# p.inst(RY(np.pi/8)(1))
# p.inst(X(0))


# CF rotation (GOOD but verbose)
p.inst(X(0))
p.inst(H(0))
p.inst(H(1))
p.inst(CNOT(1, 0))
p.inst(H(0))
p.inst(H(1))
p.inst(X(0))
p.inst(CNOT(1, 0))
p.inst(RY(-1 * np.pi/8)(0))
p.inst(CNOT(1, 0))
p.inst(RY(np.pi/8)(0))
p.inst(X(0))
p.inst(H(0))
p.inst(H(1))
p.inst(CNOT(1, 0))
p.inst(H(0))
p.inst(H(1))
p.inst(X(0))

# DE rotation (GOOD)
# p.inst(CNOT(1, 0))
# p.inst(H(0))
# p.inst(H(1))
# p.inst(CNOT(1, 0))
# p.inst(RY(np.pi/8)(1))
# p.inst(CNOT(1, 0))
# p.inst(H(0))
# p.inst(H(1))
# p.inst(RY(np.pi/8)(1))
# p.inst(CNOT(1, 0))

# DF rotation (GOOD)
# p.inst(H(0))
# p.inst(H(1))
# p.inst(CNOT(1, 0))
# p.inst(RY(np.pi/8)(1))
# p.inst(CNOT(1, 0))
# p.inst(H(0))
# p.inst(H(1))
# p.inst(RY(np.pi/8)(1))

# EF rotation (GOOD)
# p.inst(CNOT(1, 0))
# p.inst(RY(-1 * np.pi/8)(0))
# p.inst(CNOT(1, 0))
# p.inst(RY(np.pi/8)(0))


wavefunction = qvm.wavefunction(p)
print(wavefunction)
