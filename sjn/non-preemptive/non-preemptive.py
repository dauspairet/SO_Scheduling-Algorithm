class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def sjn(processes):
    n = len(processes)
    completed_processes = []
    current_time = 0
    
    while len(completed_processes) != n:
        # Filter out the processes that haven't arrived yet
        arrived_processes = [p for p in processes if p.arrival_time <= current_time and p not in completed_processes]
        
        if not arrived_processes:
            # No processes to execute, just increment the time
            current_time += 1
            continue
        
        # Find the process with the shortest burst time
        next_process = min(arrived_processes, key=lambda p: p.burst_time)
        
        # Update the process's attributes
        next_process.completion_time = current_time + next_process.burst_time
        next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
        next_process.waiting_time = next_process.turnaround_time - next_process.burst_time
        
        # Add the process to the completed list and update the current time
        completed_processes.append(next_process)
        current_time = next_process.completion_time
    
    # Calculate the average waiting time
    total_waiting_time = sum(p.waiting_time for p in completed_processes)
    avg_waiting_time = total_waiting_time / n
    
    # Print the table of processes
    print("+-----+--------------+------------+-----------------+----------------+--------------+")
    print("| PID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |")
    print("+-----+--------------+------------+-----------------+----------------+--------------+")
    for p in completed_processes:
        print(f"| {p.pid:3} | {p.arrival_time:12} | {p.burst_time:10} | {p.completion_time:15} | {p.turnaround_time:14} | {p.waiting_time:12} |")
    print("+-----+--------------+------------+-----------------+----------------+--------------+")
    print(f"Average waiting time: {avg_waiting_time:.2f}")
    
processes = [
    Process(1, 0, 8),
    Process(2, 1, 4),
    Process(3, 2, 9),
    Process(4, 3, 5),
    Process(5, 4, 2),
]
sjn(processes)

# Output
# +-----+--------------+------------+-----------------+----------------+--------------+
# | PID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |
# +-----+--------------+------------+-----------------+----------------+--------------+
# |   1 |            0 |          8 |               8 |              8 |            0 |
# |   5 |            4 |          2 |              10 |              6 |            4 |
# |   2 |            1 |          4 |              14 |             13 |            9 |
# |   4 |            3 |          5 |              19 |             16 |           11 |
# |   3 |            2 |          9 |              28 |             26 |           17 |
# +-----+--------------+------------+-----------------+----------------+--------------+
# Average waiting time: 8.20
