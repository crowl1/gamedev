import numpy as np

def sigmoid(x):
    return 1/ (1 + np.exp(-x))

training_data_input = np.array([[0, 1, 1, 0],
                        [1, 1, 1, 0],
                        [1, 0, 0, 0],
                        [0, 1, 1, 0]])

training_data_outputs = np.array([[1,0,1,0]]).T


synaptic_weights = 2 * np.random.random((4,1)) - 1

print(synaptic_weights)

for _ in range(20000):
    outputs = sigmoid(np.dot(training_data_input, synaptic_weights))

    err = training_data_outputs - outputs
    adjustments = np.dot ( training_data_input.T, err * (1 - outputs))

    synaptic_weights += adjustments

outputs += synaptic_weights

print(synaptic_weights, outputs)