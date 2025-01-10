import unittest
import sys
import os
import numpy as np

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_simulation.circuit import QuantumCircuit
from quantum_simulation.gates import X, I, H, CNOT_nq

class TestQuantumSimulationCircuit(unittest.TestCase):
    def test_initialization_gate(self):
        qc = QuantumCircuit(num_qubits=2)
        self.assertEqual(qc.num_qubits, 2)
        self.assertTrue(np.allclose(qc.state, np.array([1, 0, 0, 0], dtype=complex)))
        
    def test_add_gate(self):
        qc = QuantumCircuit(num_qubits=2)
        qc.add_gate(X, [0]) # Add Pauli-X gate
        self.assertEqual(len(qc.gates), 1)
    
    def test_delete_gate(self):
        qc = QuantumCircuit(num_qubits=2)
        qc.add_gate(X, [0])
        qc.delete_gate(X, [0])
        self.assertEqual(len(qc.gates), 0)
    
    def test_expand_gate(self):
        qc = QuantumCircuit(num_qubits=2)
        expanded_gate = qc.expand_gate(X, [0])
        expected_gate = np.kron(X, I)# Pauli-X on qubit 0, Identity on qubit 1
        # np.kron -> kronecker product
        self.assertTrue(np.allclose(expanded_gate, expected_gate))
        # np.allclose -> returns True if two arrays are element-wise equal within a tolerance.
    
    def test_apply_gate(self):
        qc = QuantumCircuit(num_qubits=1)
        qc.apply_gate(X, [0])
        expected_state = np.array([0, 1], dtype=complex)  # |1> state
        self.assertTrue(np.allclose(qc.state, expected_state))
    
    # is not working entirely
    def test_full_simulation(self):
        # simple Hadamard and Controlled-Not Gates circuit and simulate it
        qc = QuantumCircuit(num_qubits=3)
        qc.add_gate(H, [0])
        qc.add_gate(CNOT_nq(3,[0],1), [0,1])
        qc.add_gate(CNOT_nq(3,[1],2), [1,2])
        qc.simulate()
        print(qc.state)
        expected_state = np.zeros(2**3, dtype=complex)
        expected_state[0] = 1 / np.sqrt(2)  # |000>
        expected_state[7] = 1 / np.sqrt(2)  # |111>
        self.assertTrue(np.allclose(qc.state, expected_state))

if __name__ == "__main__":
    unittest.main()