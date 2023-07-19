from qiskit import QuantumCircuit, execute, BasicAer

#Building the circuits
qc1 = QuantumCircuit(2,2)
qc1.h(0)
qc1.cx(0,1)
qc1.measure([0,1], [0,1])

qc2= QuantumCircuit(2,2)
qc2.h([0,1])
qc2.measure([0,1], [0,1])

# #Setting up backends
# print("Setting up the BasicAer backend")
# print(BasicAer.backends())

#Transpiling and simulating the result from the backend
backend_sim = execute([qc1,qc2], BasicAer.get_backend("qasm_simulator"))
results_sim = backend_sim.result()

#Printing the simulated results
print("qc1 Simulated results: ", results_sim.get_counts(qc1))
print("qc2 Simulated results: ", results_sim.get_counts(qc2))