import numpy as np
from collections import Counter

def measure(state):
    probabilities = np.abs(state)**2
    return np.random.choice(len(state), p=probabilities)

def calculate_probabilities(state):
    return np.abs(state)**2

def post_measurement_state(state, measured_index):
    collapsed_state = np.zeros_like(state, dtype=complex)
    collapsed_state[measured_index] = 1
    return collapsed_state

def measure_qubits(state, qubit_indices, num_qubits):
    probabilities = calculate_probabilities(state)
    results = Counter()

    for i in range(len(state)):
        binary_state = f"{i:0{num_qubits}b}"
        measured_state = "".join([binary_state[q] for q in qubit_indices])
        results[measured_state] += probabilities[i]

    return dict(results)

def measure_and_collapse(state):
    measured_index = measure(state)
    collapsed_state = post_measurement_state(state, measured_index)
    return measured_index, collapsed_state
