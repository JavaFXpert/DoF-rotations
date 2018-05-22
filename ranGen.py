import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *
import numpy as np

qvm = api.QVMConnection()

p = pq.Program()
p.inst(X(0))

p.inst(H(0), H(1), H(2)).measure(0, 0).measure(1, 1).measure(2, 2)
#p.inst(H(0), H(1), H(2))

print(p)

num_runs = 5

classical_regs = [0, 1, 2] # A list of which classical registers to return the values of.

print(qvm.run(p, classical_regs, num_runs))

wf = qvm.wavefunction(p)
print(wf)






