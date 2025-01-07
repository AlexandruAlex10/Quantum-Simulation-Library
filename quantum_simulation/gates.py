import numpy as np

def Rx(theta):
    return np.array(
        [[np.cos(theta / 2), -1j * np.sin(theta / 2)],
         [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex
    )

def Ry(theta):
    return np.array(
        [[np.cos(theta / 2), -np.sin(theta / 2)],
         [np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex
    )

def Rz(theta):
    return np.array(
        [[np.exp(-1j * theta / 2), 0],
         [0, np.exp(1j * theta / 2)]], dtype=complex
    )

def Ph(phi):
    return np.array(
        [[1, 0],
         [0, np.exp(1j * phi)]], dtype=complex
    )

H = 1/np.sqrt(2) * np.array(
    [[1,  1],
     [1, -1]], dtype=complex
)

T = np.array(
    [[1, 0],
     [0, np.exp(1j * np.pi / 4)]], dtype=complex
)

S = np.array(
    [[1, 0],
     [0, 1j]], dtype=complex
)

I = np.array(
    [[1, 0],
     [0, 1]], dtype=complex
)

X = np.array(
    [[0, 1],
     [1, 0]], dtype=complex
)

Y = np.array(
    [[0, -1j],
     [1j, 0]], dtype=complex
)

Z = np.array(
    [[1, 0],
     [0, -1]], dtype=complex
)

CNOT_2q = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]], dtype=complex
)

def CNOT_nq(n, control, target):
    if target in control:
        raise ValueError("Target qubit cannot be one of the control qubits.")

    num_states = 2 ** n
    cnot_matrix = np.eye(num_states, dtype=complex)

    for i in range(num_states):
        binary = list(f"{i:0{n}b}")

        if all(binary[ctrl] == "1" for ctrl in control):
            binary[target] = "1" if binary[target] == "0" else "0"
            j = int("".join(binary), 2)

            cnot_matrix[i, i], cnot_matrix[i, j] = 0, 1
            cnot_matrix[j, j], cnot_matrix[j, i] = 0, 1

    return cnot_matrix