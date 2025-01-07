import numpy as np
from quantum_simulation import I, X, ket_0, ket_1

if np.allclose(I @ ket_0, ket_0) and np.allclose(I @ ket_1, ket_1):
    print("I gate works as intended")
else:
    print("I gate does not work as intended")

if np.allclose(X @ ket_0, ket_1) and np.allclose(X @ ket_1, ket_0):
    print("X gate works as intended")
else:
    print("X gate does not work as intended")
