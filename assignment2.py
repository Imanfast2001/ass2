
class System:
    def __init__(self, processes, resources):
        self.processes = processes  # List of processes
        self.resources = resources  # Dictionary of resource totals and availability

    def request_resources(self, process_id, request):
        process = self.processes[process_id]
        print(f"Process {process_id} requesting resources: {request}")
        
        can_allocate = True
        for resource, units in request.items():
            # Check if request can be granted
            if units > self.resources[resource]['available']:
                print(f"Process {process_id} must wait for resource {resource}.")
                process['waiting'][resource] = units
                can_allocate = False
            else:
                # Tentatively allocate resources
                process['waiting'][resource] = 0

        if can_allocate:
            for resource, units in request.items():
                self.resources[resource]['available'] -= units
                process['allocated'][resource] += units
            print(f"Resources allocated to Process {process_id}: {process['allocated']}")
        return can_allocate

    def release_resources(self, process_id):
        process = self.processes[process_id]
        print(f"Process {process_id} releasing resources.")
        
        for resource, units in process['allocated'].items():
            self.resources[resource]['available'] += units
            process['allocated'][resource] = 0

        print(f"Resources available: {self.resources}")

    def detect_deadlock(self):
        print("Checking for deadlocks...")
        visited = set()
        for process_id, process in self.processes.items():
            if self.is_circular(process_id, visited, set()):
                print(f"Deadlock detected involving Process {process_id}.")
                return True
        print("No deadlock detected.")
        return False

    def is_circular(self, process_id, visited, path):
        if process_id in path:
            return True
        if process_id in visited:
            return False

        visited.add(process_id)
        path.add(process_id)
        process = self.processes[process_id]

        for resource, units in process['waiting'].items():
            if units > 0:  # Process is waiting for this resource
                for other_process_id, other_process in self.processes.items():
                    if other_process_id != process_id and other_process['allocated'].get(resource, 0) > 0:
                        if self.is_circular(other_process_id, visited, path):
                            return True

        path.remove(process_id)
        return False


# Initialize the system
processes = {
    1: {'max': {'R1': 2, 'R2': 1, 'R3': 1}, 'allocated': {'R1': 0, 'R2': 0, 'R3': 0}, 'waiting': {}},
    2: {'max': {'R1': 1, 'R2': 1, 'R3': 1}, 'allocated': {'R1': 0, 'R2': 0, 'R3': 0}, 'waiting': {}},
    3: {'max': {'R1': 1, 'R2': 0, 'R3': 1}, 'allocated': {'R1': 0, 'R2': 0, 'R3': 0}, 'waiting': {}},
}

resources = {
    'R1': {'total': 3, 'available': 3},
    'R2': {'total': 2, 'available': 2},
    'R3': {'total': 2, 'available': 2},
}

system = System(processes, resources)

# Step 1: Process 1 requests resources
system.request_resources(1, {'R2': 1, 'R3': 1})
print()

# Step 2: Process 2 requests resources
system.request_resources(2, {'R2': 1, 'R3': 1})
print()

# Step 3: Process 3 requests resources
system.request_resources(3, {'R1': 1, 'R3': 1})
print()

# Check for deadlock
if system.detect_deadlock():
    print("Deadlock detected!")
else:
    print("No deadlock detected.")
