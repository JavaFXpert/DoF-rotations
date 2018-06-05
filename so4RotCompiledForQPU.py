import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

theta = Parameter('theta')

qvm = api.QVMConnection()
p = pq.Program()

# p.inst(X(0))
# p.inst(X(1))

#From CompilerConnection
p.inst(RX(np.pi/2)(0))
p.inst(RZ(1.8062906887856827)(0))
p.inst(RX(-np.pi/2)(0))
p.inst(RZ(-np.pi)(1))
p.inst(RX(1.5707963267948977)(1))
p.inst(RZ(-1.9362860827630897)(1))
p.inst(RX(np.pi/2)(1))
p.inst(CZ(1, 0))
p.inst(RX(np.pi/2)(0))
p.inst(RZ(0.2939503813270103)(0))
p.inst(RX(-np.pi/2)(0))
p.inst(RX(-np.pi/2)(1))
p.inst(RZ(0.7227342478134151)(1))
p.inst(RX(np.pi/2)(1))
p.inst(CZ(1, 0))
p.inst(RZ(3.1415926535897913)(0))
p.inst(RX(np.pi/2)(0))
p.inst(RZ(-1.8062906887856816)(0))
p.inst(RX(np.pi/2)(0))
p.inst(RX(-np.pi/2)(1))
p.inst(RZ(-1.9362860827630892)(1))
p.inst(RX(1.5707963267948968)(1))

wavefunction = qvm.wavefunction(p)
print(wavefunction)
