# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 06:28:36 2020

@author: asgun
"""

from qiskit import *

circuit = QuantumCircuit(2,2) #dois qubits
circuit.swap(0,1) #Swap qubit 0 e 1

print(circuit)

simulator = Aer.get_backend('unitary_simulator')

result = execute(circuit, backend=simulator).result()

print(result.get_unitary())
