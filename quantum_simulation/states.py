import numpy as np

ket_0 = np.array([1, 0], dtype=complex)
ket_1 = np.array([0, 1], dtype=complex)

ket_plus = (ket_0 + ket_1) / np.sqrt(2)
ket_minus = (ket_0 - ket_1) / np.sqrt(2)

ket_00 = np.kron(ket_0, ket_0)
ket_01 = np.kron(ket_0, ket_1)
ket_10 = np.kron(ket_1, ket_0)
ket_11 = np.kron(ket_1, ket_1)

bell_state = 1/np.sqrt(2) * (ket_00 + ket_11)

a, b, c, d = 0.5, 0.5, 0.5, 0.5
ket_psi = a * ket_00 + b * ket_01 + c * ket_10 + d * ket_11