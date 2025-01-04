# Necessary imports
import numpy as np

# Single-qubit states
ket_0 = np.array([1, 0], dtype=complex)  # |0>
ket_1 = np.array([0, 1], dtype=complex)  # |1>
ket_plus = (ket_0 + ket_1) / np.sqrt(2)  # |+> = H|0>
ket_minus = (ket_0 - ket_1) / np.sqrt(2)  # |-> = H|1>

# Multi-qubit states (2 qubits)
ket_00 = np.kron(ket_0, ket_0)  # |00>
ket_01 = np.kron(ket_0, ket_1)  # |01>
ket_10 = np.kron(ket_1, ket_0)  # |10>
ket_11 = np.kron(ket_1, ket_1)  # |11>

# Bell state (superposition)
bell_state = 1/np.sqrt(2) * (ket_00 + ket_11)  # (|00> + |11>)/sqrt(2)

# Arbitrary 2-qubit state (|ψ> = a|00> + b|01> + c|10> + d|11>)
a, b, c, d = 0.5, 0.5, 0.5, 0.5  # Coefficients
ket_psi = a * ket_00 + b * ket_01 + c * ket_10 + d * ket_11