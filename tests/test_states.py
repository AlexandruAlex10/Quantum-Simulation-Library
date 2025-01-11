import unittest
import sys
import os
import numpy as np

# Add the parent directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from quantum_simulation.states import ket_0, ket_01, ket_1, bell_state, ket_00, ket_11, ket_psi, ket_10


class TestQuantumStates(unittest.TestCase):
    def test_ket(self):
        self.assertTrue(np.allclose(np.kron(ket_0,ket_1), ket_01),ket_01)
    
    def test_bell_state(self):
        expected_result =(1/np.sqrt(2))*(ket_00+ket_11)
        self.assertTrue(np.allclose(bell_state, expected_result))
        
    def test_ket_psi(self):
        a, b, c, d = 0.5, 0.5, 0.5, 0.5
        result = a * ket_00 + b * ket_01 + c * ket_10 + d * ket_11
        self.assertTrue(np.allclose(ket_psi, result))
        
if __name__ == "__main__":
    unittest.main()