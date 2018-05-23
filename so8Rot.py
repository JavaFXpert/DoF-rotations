import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

theta = Parameter('theta')

anot = np.array([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

aary = np.array([[quil_cos(theta / 2), -1 * quil_sin(theta / 2), 0, 0, 0, 0, 0, 0],
                [quil_sin(theta / 2), quil_cos(theta / 2), 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]])

ccry = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, quil_cos(theta / 2), -1 * quil_sin(theta / 2)],
                [0, 0, 0, 0, 0, 0, quil_sin(theta / 2), quil_cos(theta / 2)]])

#NOT QUITE RIGHT?
cary = np.array([[1, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, quil_cos(theta / 2), -1 * quil_sin(theta / 2), 0, 0, 0],
                [0, 0, 0, quil_sin(theta / 2), quil_cos(theta / 2), 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1]])

dg_anot = DefGate('ANOT', anot)
dg_aary = DefGate('AARY', aary, [theta])
dg_ccry = DefGate('CCRY', ccry, [theta])
dg_cary = DefGate('CARY', cary, [theta])

ANOT = dg_anot.get_constructor()
AARY = dg_aary.get_constructor()
CCRY = dg_ccry.get_constructor()
CARY = dg_cary.get_constructor()

qvm = api.QVMConnection()
p = pq.Program()

p.inst(dg_anot)
p.inst(dg_aary)
p.inst(dg_ccry)
p.inst(dg_cary)

# p.inst(X(0))
p.inst(X(1))
p.inst(X(2))

# CD rotation
# p.inst(AARY(np.pi/4)(2, 1, 0))

# CE rotation
# p.inst(AARY(np.pi/4)(2, 0, 1))

# CF rotation
# p.inst(CNOT(1, 0))
# p.inst(AARY(np.pi/4)(0, 2, 1))
# p.inst(CNOT(1, 0))

# CG rotation
# p.inst(AARY(np.pi/4)(0, 1, 2))

# CA rotation
# p.inst(CNOT(2, 0))
# p.inst(AARY(np.pi/4)(0, 1, 2))
# p.inst(CNOT(2, 0))

# CB rotation
# p.inst(CNOT(2, 1))
# p.inst(AARY(np.pi/4)(0, 1, 2))
# p.inst(CNOT(2, 1))

# CC' rotation
# p.inst(CNOT(1, 0))
# p.inst(CNOT(1, 2))
# p.inst(AARY(np.pi/4)(0, 2, 1))
# p.inst(CNOT(1, 2))
# p.inst(CNOT(1, 0))

# DE rotation
# p.inst(CNOT(1, 0))
# p.inst(CRY(np.pi/4)(0, 1))
# p.inst(CNOT(1, 0))

# DF rotation
# p.inst(X(2))
# p.inst(CCRY(np.pi/4)(0, 2, 1))
# p.inst(X(2))

# DA rotation
# p.inst(X(1))
# p.inst(CCRY(np.pi/4)(0, 1, 2))
# p.inst(X(1))

# DB rotation
p.inst(CNOT(1, 0))
p.inst(ANOT(1, 2))
p.inst(CCRY(np.pi/4)(0, 2, 1))
p.inst(ANOT(1, 2))
p.inst(CNOT(1, 0))

# DE rotation
# p.inst(ANOT(1, 0))
# p.inst(AARY(np.pi/4)(0, 2, 1))
# p.inst(ANOT(1, 0))

# DG rotation
# p.inst(ANOT(2, 0))
# p.inst(AARY(np.pi/4)(0, 1, 2))
# p.inst(ANOT(2, 0))

# DC' rotation
# p.inst(ANOT(1, 2))
# p.inst(CCRY(np.pi/4)(0, 2, 1))
# p.inst(ANOT(1, 2))

# EF rotation
# p.inst(X(2))
# p.inst(CCRY(np.pi/4)(1, 2, 0))
# p.inst(X(2))

# EG rotation
# p.inst(ANOT(2, 1))
# p.inst(AARY(np.pi/4)(0, 1, 2))
# p.inst(ANOT(2, 1))

# EB rotation
# p.inst(X(0))
# p.inst(CCRY(np.pi/4)(0, 1, 2))
# p.inst(X(0))

# EC' rotation
# p.inst(ANOT(0, 2))
# p.inst(CCRY(np.pi/4)(1, 2, 0))
# p.inst(ANOT(0, 2))

# FG rotation
# p.inst(CARY(np.pi/4)(2, 1, 0))

# FA rotation
# p.inst(CNOT(2, 1))
# p.inst(CCRY(np.pi/4)(0, 1, 2))
# p.inst(CNOT(2, 1))

# FB rotation
# p.inst(CNOT(2, 0))
# p.inst(CCRY(np.pi/4)(0, 1, 2))
# p.inst(CNOT(2, 0))

# FC' rotation
# p.inst(CCRY(np.pi/4)(0, 1, 2))

# GA rotation
# p.inst(X(1))
# p.inst(CCRY(np.pi/4)(1, 2, 0))
# p.inst(X(1))

# GB rotation
# p.inst(X(0))
# p.inst(CCRY(np.pi/4)(0, 2, 1))
# p.inst(X(0))

# GC' rotation
# p.inst(ANOT(1, 0))
# p.inst(CCRY(np.pi/4)(0, 2, 1))
# p.inst(ANOT(1, 0))

# AB rotation
# p.inst(CNOT(1, 0))
# p.inst(CCRY(np.pi/4)(0, 2, 1))
# p.inst(CNOT(1, 0))

# AC' rotation
# p.inst(CCRY(np.pi/4)(0, 2, 1))

# BC' rotation
# p.inst(CCRY(np.pi/4)(1, 2, 0))

wavefunction = qvm.wavefunction(p)
print(wavefunction)

