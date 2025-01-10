import numpy as np
from .measurements import measure
from .gates import I

class QuantumCircuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1  # Initialize to |0...0> state
        self.gates = []  # List of gates to be applied

    def add_gate(self, gate, qubits):
        self.gates.append((gate, qubits))
    
    def delete_gate(self, gate, qubits):
        if (gate, qubits) in self.gates:
            self.gates.remove((gate, qubits))

    def apply_gate(self, gate, qubits):
        full_gate = self.expand_gate(gate, qubits)
        # matrix multiplication in numpy
        print(self.state)
        print(full_gate)
        self.state = full_gate @ self.state

    def expand_gate(self, gate, qubits):
        num_qubits = self.num_qubits
        full_gate = 1
        for i in range(num_qubits):
            if i in qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, I)
        return full_gate

    def simulate(self):
        for gate, qubits in self.gates:
            self.apply_gate(gate, qubits)
        return self.state

    def measure_all(self):
        return measure(self.state)

    def __str__(self):
        return f"QuantumCircuit(num_qubits={self.num_qubits}, gates={len(self.gates)})"
