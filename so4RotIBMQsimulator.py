from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import available_backends, execute

from math import *
import numpy as np

q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)

qc.x(q[0])
qc.x(q[1])

# CD rotation (GOOD)
qc.x(q[1])
qc.cx(q[1], q[0])
qc.u3(-np.pi/8, 0, 0, q[0])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[0])
qc.x(q[1])

# CE rotation (GOOD)
qc.x(q[0])
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.u3(np.pi/8, 0, 0, q[1])
qc.x(q[0])


# CF rotation (GOOD)
qc.x(q[0])
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.x(q[0])
qc.cx(q[1], q[0])
qc.u3(-np.pi/8, 0, 0, q[0])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[0])
qc.x(q[0])
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.x(q[0])


# DE rotation (GOOD)
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.u3(np.pi/8, 0, 0, q[1])
qc.cx(q[1], q[0])


# DF rotation (GOOD)
qc.h(q[0])
qc.h(q[1])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[1])
qc.cx(q[1], q[0])
qc.h(q[0])
qc.h(q[1])
qc.u3(np.pi/8, 0, 0, q[1])


# EF rotation (GOOD)
qc.cx(q[1], q[0])
qc.u3(-np.pi/8, 0, 0, q[0])
qc.cx(q[1], q[0])
qc.u3(np.pi/8, 0, 0, q[0])

qc.measure(q, c)

# Compile and run the Quantum circuit on a simulator backend
job_sim = execute(qc, "local_qasm_simulator", shots = 1000)
sim_result = job_sim.result()

# Show the results
print("simulation: ", sim_result)
print(sim_result.get_counts(qc))