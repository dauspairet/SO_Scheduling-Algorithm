class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = None
        self.turnaround_time = None
        self.waiting_time = None
        
    def __str__(self):
        return f"Process({self.pid}, {self.arrival_time}, {self.burst_time})"

def sjf(processes):
    # Sort processes by arrival time and burst time
    processes = sorted(processes, key=lambda p: (p.arrival_time, p.burst_time))
    
    # Initialize variables
    current_time = 0
    total_waiting_time = 0
    num_processes = len(processes)
    completed_processes = []
    
    while len(completed_processes) < num_processes:
        # Check for processes that have arrived
        ready_processes = [p for p in processes if p.arrival_time <= current_time and p not in completed_processes]
        
        if not ready_processes:
            current_time += 1
            continue
        
        # Get the process with the shortest burst time
        next_process = min(ready_processes, key=lambda p: p.burst_time)
        next_process.waiting_time = current_time - next_process.arrival_time
        next_process.completion_time = current_time + next_process.burst_time
        next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
        
        # Update variables
        completed_processes.append(next_process)
        total_waiting_time += next_process.waiting_time
        current_time = next_process.completion_time
        
    # Calculate average waiting time
    average_waiting_time = total_waiting_time / num_processes
    
    return completed_processes, average_waiting_time

# Example usage:
processes = [
    Process(1, 0, 5),
    Process(2, 1, 2),
    Process(3, 2, 1),
    Process(4, 3, 4),
    Process(5, 4, 3)
]

completed_processes, average_waiting_time = sjf(processes)

# Print results
print("Completed Processes:")
for process in completed_processes:
    print(f"PID: {process.pid}, Arrival Time: {process.arrival_time}, Burst Time: {process.burst_time}, "
          f"Completion Time: {process.completion_time}, Turnaround Time: {process.turnaround_time}, "
          f"Waiting Time: {process.waiting_time}")
print(f"Average Waiting Time: {average_waiting_time}")

# Completed Processes:
# PID: 1, Arrival Time: 0, Burst Time: 5, Completion Time: 5, Turnaround Time: 5, Waiting Time: 0
# PID: 3, Arrival Time: 2, Burst Time: 1, Completion Time: 6, Turnaround Time: 4, Waiting Time: 3
# PID: 2, Arrival Time: 1, Burst Time: 2, Completion Time: 8, Turnaround Time: 7, Waiting Time: 5
# PID: 5, Arrival Time: 4, Burst Time: 3, Completion Time: 11, Turnaround Time: 7, Waiting Time: 4
# PID: 4, Arrival Time: 3, Burst Time: 4, Completion Time: 15, Turnaround Time: 12, Waiting Time: 8
# Average Waiting Time: 4.0
