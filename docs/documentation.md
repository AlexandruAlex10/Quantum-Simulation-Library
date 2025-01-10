In order to build and run this project, the following libraries must be installed: python (+ its default libraries), numpy, setuptools, wheel and of course, own made quantum_simulation library.

To install numpy/wheel (and any other libraries that you may need), you can run pip install <library> in a terminal.
To install quantum_simulation library, run in a terminal the following commands (make sure to be inside the project directory where setup.py file is located!):
    python setup.py bdist_wheel sdist
    pip install .

The project is made of:
    - "docs" folder: in here you can find references to the theory that was used in implementing this project and also explanations about the implementation itself.
    - "quantum_simulation" folder: the actual code implementation of the project, consisting of a couple of different files, each having its own purpose.
    - "tests" folder: some tests were implemented in order to check that the code implementation was done correctly. 
    - "examples" folder: some applications resulted from implementing the project.
    - other useful files.

Quantum Simulation Library contains:
    - __init__.py file: this file, alongside with setup.py, are used for creating and exporting quantum_simulation package in other areas of the project, such as "tests" and "examples" folders.

    - circuit.py file: it contains a class called "QuantumCircuit" that is used for creating instances of quantum circuits. It contains the following functions:
        -> __init__: initializes a quantum circuit with a given number of qubits.
                    parameters: num_qubits (int): The number of qubits in the circuit.
        -> add_gate: add a gate to the circuit.
                    parameters: gate (np.ndarray): The gate matrix.
                                qubits (list[int]): The indices of qubits the gate acts on.
        -> apply_gate: apply a gate to the current state.
                    parameters: gate (np.ndarray): The gate matrix.
                                qubits (list[int]): The indices of qubits the gate acts on.
        -> expand_gate: expand a gate to act on the full system of qubits.
                    parameters: gate (np.ndarray): The gate matrix.
                                qubits (list[int]): The indices of qubits the gate acts on.
                    returns: np.ndarray: The expanded gate matrix.
        -> simulate: simulate the circuit by applying all gates to the initial state.
                    returns: np.ndarray: The final quantum state vector.
        -> measure_all: measure all qubits in the circuit.
                    returns: int: The measured basis state as an integer.
        -> __str__: generate a string representation of the circuit.
                    returns: str: A textual representation of the circuit.

    - gates.py file: it contains several gate declarations/declaration functions.
        -> Rx Gate (Rotation around X-axis): this gate rotates a qubit around the X axis of the Bloch sphere by an angle θ.
        -> Ry Gate (Rotation around Y-axis): this gate rotates a qubit around the Y axis of the Bloch sphere by an angle θ.
        -> Rz Gate (Rotation around Z-axis): this gate rotates a qubit around the Z axis of the Bloch sphere by an angle θ.
        -> Ph Gate (Phase Gate): adds a phase shift of ϕ to the ∣1⟩ state.
        -> H Gate (Hadamard Gate): a single-qubit gate that creates a superposition of quantum states.
        -> T Gate: applies a phase of π/4 to the ∣1⟩ state.
        -> S Gate: applies a phase of π/2 to the ∣1⟩ state.
        -> I Gate (Identity Gate): a single-qubit gate that does nothing to the quantum state.
        -> X (Pauli-X Gate): a single-qubit gate equivalent to a classical NOT gate (flips ∣0⟩ to ∣1⟩ and vice versa).
        -> Y (Pauli-Y Gate): a single-qubit gate that combines the X and Z gates with a phase factor.
        -> Z (Pauli-Z Gate): a single-qubit gate that applies a phase shift of π to the state ∣1⟩.
        -> CNOT_2q Gate (most common Controlled-X Gate): a 2-qubit gate that flips the second qubit (target) if the first qubit (control) is ∣1⟩.
        -> CNOT_nq Gate (Controlled-X Gate for n qubits): generates a CNOT gate matrix for n qubits with multiple control qubits.
                    parameters: n (int): Total number of qubits.
                                control_qubits (list[int]): List of indices for the control qubits (0-indexed).
                                target_qubit (int): Index of the target qubit (0-indexed).
                    returns: np.ndarray: The multi-control CNOT gate matrix of size 2^n x 2^n.

    - measurements.py: it contains several functions that handle quantum measurement operations.
        -> measure: perform a measurement on a quantum state in the computational basis.
                    parameters: state (np.ndarray): The quantum state vector.
                    returns: int: The measured basis state as an integer.
        -> calculate_probabilities: calculate the probabilities of each basis state in a quantum state.
                                    parameters: state (np.ndarray): The quantum state vector.
                                    returns: np.ndarray: An array of probabilities for each basis state.
        -> post_measurement_state: get the post-measurement state after collapsing to a specific basis state.
                                parameters: state (np.ndarray): The quantum state vector.
                                            measured_index (int): The index of the measured basis state.
                                returns: np.ndarray: The collapsed state vector.
        -> measure_qubits: measure specific qubits in a quantum state.
                        parameters: state (np.ndarray): The quantum state vector.
                                    qubit_indices (list[int]): Indices of qubits to measure.
                                    num_qubits (int): Total number of qubits.
                        returns: dict: A dictionary with measurement outcomes and probabilities.
        -> measure_and_collapse: simulate a full measurement process, including state collapse.
                                parameters: state (np.ndarray): The quantum state vector.
                                returns: tuple[int, np.ndarray]: The measured basis state as an integer and the collapsed state vector.

    - states.py: it contains several declarations of different quantum states.
        -> ket_0: |0> state.
        -> ket_1: |1> state.
        -> ket_plus: |+> = 1/sqrt(2) * (|0> + |1>) state.
        -> ket_minus: |-> = 1/sqrt(2) * (|0> - |1>) state.
        -> ket_00: |00> state.
        -> ket_01: |01> state.
        -> ket_10: |10> state.
        -> ket_11: |11> state.
        -> bell_state: 1/sqrt(2) * (|00> + |11>) state.
        -> ket_psi: 1/2 * (|00> + |01> + |10> + |11>) state.
