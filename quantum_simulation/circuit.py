import numpy as np
from .measurements import measure

class QuantumCircuit:
    """
    The `QuantumCircuit` class represents a quantum circuit in Python for simulating quantum
    computations. Here is a breakdown of its key functionalities:
    """
    
    def __init__(self, num_qubits):
        """
        The function initializes a quantum circuit with a specified number of qubits and sets the
        initial state to |0...0>.
        
        :param num_qubits: The `num_qubits` parameter in the `__init__` method is used to specify the
        number of qubits in the quantum circuit. It determines the size of the quantum state vector and
        initializes it to represent the |0...0⟩ state, where all qubits are in the |0
        """
        
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1  # Initialize to |0...0> state
        self.gates = []  # List of gates to be applied

    def add_gate(self, gate, qubits):
        """
        The `add_gate` method in the `QuantumCircuit` class is used to add a gate operation to the
        quantum circuit. It takes two parameters: `gate` which represents the quantum gate to be
        applied, and `qubits` which specifies the qubits on which the gate will act.
        """
        
        self.gates.append((gate, qubits))
    
    def delete_gate(self, gate, qubits):
        """
        The `delete_gate` method in the `QuantumCircuit` class is designed to remove a specific gate
        operation from the list of gates to be applied in the quantum circuit. It takes two
        parameters: `gate`, which represents the quantum gate to be removed, and `qubits`, which
        specifies the qubits on which the gate was intended to act.
        """

        if (gate, qubits) in self.gates:
            self.gates.remove((gate, qubits))

    def apply_gate(self, gate, qubits):
        """
        The `apply_gate` method in the `QuantumCircuit` class is responsible for applying a
        specified quantum gate operation to the quantum state vector of the circuit.
        """

        full_gate = self.expand_gate(gate, qubits)
        self.state = full_gate @ self.state # Matrix multiplication in numpy

    def expand_gate(self, gate, qubits):
        """
        The `expand_gate` method creates the full gate matrix that acts on all qubits.
        If the gate is already of size 2^n x 2^n, it skips expansion.
        """

        num_qubits = self.num_qubits
        dim = 2**num_qubits

        if gate.shape == (dim, dim): # If the gate is already full-sized, return it directly
            return gate

        identity = np.eye(2, dtype=complex)
        full_gate = 1

        for i in range(num_qubits):
            if i in qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, identity)

        return full_gate

    def simulate(self):
        """
        The `simulate` method in the `QuantumCircuit` class is iterating over the list of gates
        stored in the circuit and applying each gate operation to the quantum state vector. It does
        this by calling the `apply_gate` method for each gate in the list. After applying all the
        gates, it returns the final quantum state vector representing the result of simulating the
        quantum circuit up to that point.
        """
        
        for gate, qubits in self.gates:
            self.apply_gate(gate, qubits)
        return self.state

    def measure_all(self):
        return measure(self.state)

    def __str__(self):
        return f"QuantumCircuit(num_qubits={self.num_qubits}, gates={len(self.gates)})"
