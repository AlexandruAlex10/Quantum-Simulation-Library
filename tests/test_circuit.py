import unittest
import sys
import os
import numpy as np

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_simulation.circuit import QuantumCircuit
from quantum_simulation.gates import X, Z, I, H, CNOT

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
        expected_gate = np.kron(X, I) # Pauli-X on qubit 0, Identity on qubit 1; np.kron -> kronecker product
        self.assertTrue(np.allclose(expanded_gate, expected_gate)) # np.allclose -> returns True if two arrays are element-wise equal within a tolerance.
    
    def test_apply_gate(self):
        qc = QuantumCircuit(num_qubits=1)
        qc.apply_gate(X, [0])
        expected_state = np.array([0, 1], dtype=complex)  # |1> state
        self.assertTrue(np.allclose(qc.state, expected_state))
    
    def test_full_simulation_1(self):
        qc = QuantumCircuit(num_qubits=5)
        qc.add_gate(X, [0])
        qc.add_gate(X, [1])
        qc.add_gate(Z, [1])
        qc.add_gate(X, [2])
        qc.add_gate(X, [2])
        qc.add_gate(I, [3])
        qc.add_gate(Z, [4])
        qc.add_gate(X, [4])
        qc.add_gate(Z, [4])
        qc.add_gate(X, [4])
        qc.simulate()
        expected_state = np.zeros(2**5, dtype=complex)
        expected_state[24] = 1  # |11000>
        self.assertTrue(np.allclose(qc.state, expected_state))

    def test_full_simulation_2(self):
        qc = QuantumCircuit(num_qubits=3)
        qc.add_gate(H, [0])
        qc.add_gate(CNOT(3,[0],1), [0,1])
        qc.add_gate(CNOT(3,[1],2), [1,2])
        qc.simulate()
        expected_state = np.zeros(2**3, dtype=complex)
        expected_state[0] = 1 / np.sqrt(2)  # 1/sqrt(2) * |000>
        expected_state[7] = 1 / np.sqrt(2)  # 1/sqrt(2) * |111>
        self.assertTrue(np.allclose(qc.state, expected_state))

    def test_full_simulation_3(self):
        qc = QuantumCircuit(num_qubits=5)
        qc.add_gate(X, [0])
        qc.add_gate(X, [1])
        qc.add_gate(X, [2])
        qc.add_gate(X, [3])
        qc.add_gate(X, [4])
        qc.add_gate(CNOT(5,[0,1,2,3],4), [0,1,2,3,4])
        qc.add_gate(CNOT(5,[0],1), [0,1])
        qc.add_gate(CNOT(5,[2],3), [2,3])
        qc.add_gate(CNOT(5,[4],3), [3,4])
        qc.add_gate(CNOT(5,[4],2), [2,4])
        qc.add_gate(CNOT(5,[4],1), [1,4])
        qc.add_gate(CNOT(5,[4],0), [0,4])
        qc.simulate()
        expected_state = np.zeros(2**5, dtype=complex)
        expected_state[20] = 1 # |10100>
        self.assertTrue(np.allclose(qc.state, expected_state))

if __name__ == "__main__":
    unittest.main()