import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

theta = Parameter('theta')

cry = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, quil_cos(theta / 2), -1 * quil_sin(theta / 2)], [0, 0, quil_sin(theta / 2), quil_cos(theta / 2)]])
acry = np.array([[quil_cos(theta / 2), -1 * quil_sin(theta / 2), 0, 0], [quil_sin(theta / 2), quil_cos(theta / 2), 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

dg_cry = DefGate('CRY', cry, [theta])
dg_acry = DefGate('ACRY', acry, [theta])

CRY = dg_cry.get_constructor()
ACRY = dg_acry.get_constructor()

qvm = api.QVMConnection()
p = pq.Program()

p.inst(dg_cry)
p.inst(dg_acry)

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

# Corresponding rotations in Julia Language
# matrix = eye(4)
## rotMatrix = eye(4)
# r1=r2=r3=r4=r5=r6=22.5
# rotMatrix = transpose([cosd(r1) -sind(r1) 0 0; sind(r1) cosd(r1) 0 0; 0 0 1 0; 0 0 0 1]) *
# transpose([cosd(r2) 0 -sind(r2) 0; 0 1 0 0; sind(r2) 0 cosd(r2) 0; 0 0 0 1]) *
# transpose([cosd(r3) 0 0 -sind(r3); 0 1 0 0; 0 0 1 0; sind(r3) 0 0 cosd(r3)]) *
# transpose([1 0 0 0; 0 cosd(r4) -sind(r4) 0; 0 sind(r4) cosd(r4) 0; 0 0 0 1]) *
# transpose([1 0 0 0; 0 cosd(r5) 0 -sind(r5); 0 0 1 0; 0 sind(r5) 0 cosd(r5)]) *
# transpose([1 0 0 0; 0 1 0 0; 0 0 cosd(r6) -sind(r6); 0 0 sind(r6) cosd(r6)]) *
# matrix