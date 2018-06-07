import pyquil.quil as pq
from pyquil.parameters import Parameter, quil_sin, quil_cos
from pyquil.quilbase import DefGate
import pyquil.api as api
from pyquil.gates import *
import numpy as np

#FOR COMPILERCONNECTION
from pyquil.api import CompilerConnection, get_devices
devices = get_devices(as_dict=True)
#devices = get_devices(as_dict=True)['8Q-Agave']
print(devices)
#acorn = devices['19Q-Acorn']
agave = devices['8Q-Agave']
compiler = CompilerConnection(agave)


theta = Parameter('theta')

############yrot = np.pi/8
yrot = -np.pi/(8)

#qvm = api.QVMConnection()
qpu = api.QPUConnection(agave)
p = pq.Program()

# p.inst(X(0))
# p.inst(X(1))

# CD rotation (GOOD)
p.inst(X(1))
p.inst(CNOT(1, 0))
p.inst(RY(-1 * yrot)(0))
p.inst(CNOT(1, 0))
p.inst(RY(yrot)(0))
p.inst(X(1))


# CE rotation (GOOD)
p.inst(X(0))
p.inst(CNOT(0, 1))
p.inst(RY(-1 * yrot)(1))
p.inst(CNOT(0, 1))
p.inst(RY(yrot)(1))
p.inst(X(0))


# CF rotation (GOOD)
p.inst(X(0))
p.inst(CNOT(0, 1))
p.inst(X(0))
p.inst(CNOT(1, 0))
p.inst(RY(-1 * yrot)(0))
p.inst(CNOT(1, 0))
p.inst(RY(yrot)(0))
p.inst(X(0))
p.inst(CNOT(0, 1))
p.inst(X(0))

# DE rotation (GOOD)
p.inst(CNOT(1, 0))
p.inst(CNOT(0, 1))
p.inst(RY(-1 * yrot)(1))
p.inst(CNOT(0, 1))
p.inst(RY(yrot)(1))
p.inst(CNOT(1, 0))

# DF rotation (GOOD)
p.inst(CNOT(0, 1))
p.inst(RY(-1 * yrot)(1))
p.inst(CNOT(0, 1))
p.inst(RY(yrot)(1))

# EF rotation (GOOD)
p.inst(CNOT(1, 0))
p.inst(RY(-1 * yrot)(0))
p.inst(CNOT(1, 0))
p.inst(RY(yrot)(0))

# wavefunction = qvm.wavefunction(p)
# print(wavefunction)


#FOR COMPILERCONNECTION
# job_id = compiler.compile_async(p)
# job = compiler.wait_for_job(job_id)
#
# print('compiled quil', job.compiled_quil())
# print('gate volume', job.gate_volume())
# print('gate depth', job.gate_depth())
# print('topological swaps', job.topological_swaps())
# print('program fidelity', job.program_fidelity())
# print('multiqubit gate depth', job.multiqubit_gate_depth())
#
#res = qpu.run_and_measure(p, [1, 0], trials=1000)
res = qpu.run(p, [1, 0], trials=1000)
print(res)
