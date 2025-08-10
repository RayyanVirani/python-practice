# All Libraries Imported
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import clear_output
from qiskit_machine_learning.utils import algorithm_globals
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit_machine_learning.circuit.library import QNNCircuit
from qiskit_machine_learning.algorithms import VQR
from qiskit_machine_learning.optimizers import COBYLA
import time
from mpl_toolkits.mplot3d import Axes3D

algorithm_globals.random_seed = 50

# Data Set Loaded
df = pd.read_csv(r"D:\downloads\Dataset 2.csv")  # make sure file path is correct
x = df["x"].to_numpy()
y = df["y"].to_numpy()
z = df["z"].to_numpy()

# Scale x, y -> [0, 2π]
# Scale z -> [-1, 1]
scaler_XY = MinMaxScaler(feature_range=(0, 2*np.pi))
XY_scaled = scaler_XY.fit_transform(np.column_stack((x, y)))

# Scale z -> [-1, 1]
scaler_Z = MinMaxScaler(feature_range=(-1, 1))
Z_scaled = scaler_Z.fit_transform(z.reshape(-1, 1)).flatten()

# ===== Quantum parameters =====
param_x = Parameter("x")  # Feature 1
param_y = Parameter("y")  # Feature 2

# Feature map (2 qubits)
feature_map = QuantumCircuit(2, name="fm")
feature_map.ry(param_x, 0)
feature_map.ry(param_y, 1)
feature_map.cx(0, 1)
feature_map.barrier()

# Ansatz
param_w1 = Parameter("w1")
param_w2 = Parameter("w2")
ansatz = QuantumCircuit(2, name="ansatz")
ansatz.ry(param_w1, 0)
ansatz.ry(param_w2, 1)
ansatz.cx(0, 1)

# QNN Circuit
qnn_circuit = QNNCircuit(feature_map=feature_map, ansatz=ansatz)

# ===== Callback for optimization graph =====
objective_func_vals = []

def callback_graph(weights, obj_func_eval):
    objective_func_vals.append(obj_func_eval)

# ===== Train Quantum Regressor =====
regressor = VQR(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=COBYLA(maxiter=20),
    callback=callback_graph
)

regressor.fit(XY_scaled, Z_scaled)
# ===== Predictions =====
Z_pred = regressor.predict(XY_scaled)

# ===== Plot in 3D =====
plt.figure(figsize=(6,4))
plt.plot(range(len(objective_func_vals)), objective_func_vals, 'b-')
plt.title("Objective function value against iteration")
plt.xlabel("Iteration")
plt.ylabel("Objective function value")
plt.grid(True)
plt.show()
