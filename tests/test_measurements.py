import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_simulation.gates import *
from quantum_simulation.circuit import QuantumCircuit
from quantum_simulation.measurements import *


class TestQuantumSimulationMeasurements(unittest.TestCase):
    #  define a quantum circuit made of one qubit, one bit for measurement and an X-gate. Measure the state
    def test_measurement(self):
        qc = QuantumCircuit(1)
        qc.add_gate(X, [0])
        qc.simulate()
        self.assertEqual(measure(qc.state), 1)
    
    def test_calculate_probabilities(self):
        qc = QuantumCircuit(3)
        qc.add_gate(H, [0])
        qc.add_gate(Z, [0])
        qc.add_gate(Y, [0])
        qc.simulate()
        expected_result =  np.array([1/2, 0,  0,  0,  1/2, 0,  0,  0 ])
        self.assertTrue(np.allclose(calculate_probabilities(qc.state), expected_result))
        
    def test_post_measurement_state(self):
        qc = QuantumCircuit(3)
        qc.add_gate(H, [0])
        qc.add_gate(H, [0])
        qc.add_gate(Z, [0])
        qc.add_gate(Z, [0])
        qc.add_gate(Y, [0])
        qc.add_gate(Y, [0])
        qc.simulate()
        expected_result =  np.array([0, 1, 0, 0, 0, 0, 0, 0 ], dtype=complex)
        self.assertTrue(np.allclose(post_measurement_state(qc.state, 1), expected_result))
if __name__ == "__main__":
    unittest.main()