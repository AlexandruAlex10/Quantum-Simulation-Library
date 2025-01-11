import numpy as np
from quantum_simulation import H, I, X, Z, CNOT, ket_0, ket_1, ket_plus, ket_minus, ket_00, ket_01, ket_10, ket_11

if np.allclose(H @ ket_0, ket_plus) and np.allclose(H @ ket_1, ket_minus):
    print("H gate test passed!")
else:
    print("H gate test failed!")

if np.allclose(I @ ket_0, ket_0) and np.allclose(I @ ket_1, ket_1) and np.allclose(I @ ket_plus, ket_plus) and np.allclose(I @ ket_minus, ket_minus):
    print("I gate test passed!")
else:
    print("I gate test failed!")

if np.allclose(X @ ket_0, ket_1) and np.allclose(X @ ket_1, ket_0):
    print("X gate test passed!")
else:
    print("X gate test failed!")

if np.allclose(Z @ ket_0, ket_0) and np.allclose(Z @ ket_1, -1 * ket_1):
    print("Z gate test passed!")
else:
    print("Z gate test failed!")

if np.allclose(CNOT(2, [0], 1) @ ket_00, ket_00) and np.allclose(CNOT(2, [0], 1) @ ket_01, ket_01) and np.allclose(CNOT(2, [0], 1) @ ket_10, ket_11) and np.allclose(CNOT(2, [0], 1) @ ket_11, ket_10):
    print("CNOT gate test 1 passed!")
else:
    print("CNOT gate test 1 failed!")

if np.allclose(CNOT(2, [1], 0) @ ket_00, ket_00) and np.allclose(CNOT(2, [1], 0) @ ket_01, ket_11) and np.allclose(CNOT(2, [1], 0) @ ket_10, ket_10) and np.allclose(CNOT(2, [1], 0) @ ket_11, ket_01):
    print("CNOT gate test 2 passed!")
else:
    print("CNOT gate test 2 failed!")