# Necessary imports
import numpy as np

# Rx Gate (Rotation around X-axis)
def Rx(theta):
    return np.array(
        [[np.cos(theta / 2), -1j * np.sin(theta / 2)],
         [-1j * np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex
    )

# Ry Gate (Rotation around Y-axis)
def Ry(theta):
    return np.array(
        [[np.cos(theta / 2), -np.sin(theta / 2)],
         [np.sin(theta / 2), np.cos(theta / 2)]], dtype=complex
    )

# Rz Gate (Rotation around Z-axis)
def Rz(theta):
    return np.array(
        [[np.exp(-1j * theta / 2), 0],
         [0, np.exp(1j * theta / 2)]], dtype=complex
    )

# Ph Gate (Phase Gate)
def Ph(phi):
    return np.array(
        [[1, 0],
         [0, np.exp(1j * phi)]], dtype=complex
    )

# Hadamard Gate
H = 1/np.sqrt(2) * np.array(
    [[1,  1],
     [1, -1]], dtype=complex
)

# T Gate
T = np.array(
    [[1, 0],
     [0, np.exp(1j * np.pi / 4)]], dtype=complex
)

# S Gate
S = np.array(
    [[1, 0],
     [0, 1j]], dtype=complex
)

# Identity Gate (I)
I = np.array(
    [[1, 0],
     [0, 1]], dtype=complex
)

# Pauli-X Gate
X = np.array(
    [[0, 1],
     [1, 0]], dtype=complex
)

# Pauli-Y Gate
Y = np.array(
    [[0, -1j],
     [1j, 0]], dtype=complex
)

# Pauli-Z Gate
Z = np.array(
    [[1, 0],
     [0, -1]], dtype=complex
)

# CNOT Gate (Controlled-X) for 2 qubits
CNOT_2q = np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 0]], dtype=complex
)

# CNOT Gate (Controlled-X) for n qubits and m control qubits
def CNOT_nq(n, control, target):
    if target in control:
        raise ValueError("Target qubit cannot be one of the control qubits.")

    # Number of states in the system (2^n)
    num_states = 2 ** n

    # Initialize the identity matrix for the n-qubit system
    cnot_matrix = np.eye(num_states, dtype=complex)

    # Iterate through all possible basis states
    for i in range(num_states):
        binary = list(f"{i:0{n}b}")  # Binary representation of the state
        
        # Check if all control qubits are in the |1> state
        if all(binary[ctrl] == "1" for ctrl in control):
            # Flip the target qubit
            binary[target] = "1" if binary[target] == "0" else "0"
            j = int("".join(binary), 2)  # Convert modified binary back to an integer
            
            # Swap the rows in the matrix
            cnot_matrix[i, i], cnot_matrix[i, j] = 0, 1
            cnot_matrix[j, j], cnot_matrix[j, i] = 0, 1

    return cnot_matrix