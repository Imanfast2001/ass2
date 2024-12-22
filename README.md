Resource Allocation and Deadlock Detection Simulator
- Overview -
The Resource Allocation and Deadlock Detection Simulator is a Python application designed to simulate a system where multiple processes share a fixed number of resources. It helps users understand how deadlocks occur, implement basic resource allocation systems, and detect deadlocks using a simple detection algorithm.

Problem Statement:
In systems with shared resources, processes often contend for limited resources, potentially leading to deadlock—a state where no process can proceed because they are waiting for resources held by others. This simulator models such scenarios, demonstrates resource allocation, and helps detect deadlocks in a controlled environment.

Intended Audience:
Students: Learn about resource allocation and deadlock concepts in Operating Systems.
Educators: Use as a teaching aid for demonstrating resource contention and deadlock detection.
Software Engineers: Experiment with resource allocation logic and algorithms.

Features
Process Simulation:

Simulate multiple processes with maximum demand, current allocation, and pending requests.
Resource Management:

Manage multiple resource types with total and available units.
Allocate resources dynamically based on requests.
Deadlock Detection:

Implements a basic detection algorithm to identify circular waiting among processes.
Provides detailed insights into deadlock scenarios.
Step-by-Step Simulation:

Observe how each process requests and releases resources.
Detect deadlocks after each allocation or release operation.

Running the Simulator:
Open the resource_allocation_simulator.py file in your Python IDE.
Run the file.
Observe the step-by-step simulation output in the terminal.
