from queue import PriorityQueue

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        
    def __lt__(self, other):
        return self.burst_time < other.burst_time
    
def sjf_preemptive(processes):
    ready_queue = PriorityQueue()
    current_time = 0
    total_waiting_time = 0
    num_processes = len(processes)
    completed_processes = []
    current_process = None
    
    while len(completed_processes) < num_processes:
        for process in processes:
            if process.arrival_time == current_time:
                ready_queue.put(process)
                
        if current_process is not None:
            ready_queue.put(current_process)
            current_process = None
            
        if ready_queue.empty():
            current_time += 1
            continue
            
        next_process = ready_queue.get()
        next_process.burst_time -= 1
        
        if next_process.burst_time == 0:
            next_process.completion_time = current_time + 1
            next_process.turnaround_time = next_process.completion_time - next_process.arrival_time
            next_process.waiting_time = next_process.turnaround_time - next_process.burst_time
            total_waiting_time += next_process.waiting_time
            completed_processes.append(next_process)
        else:
            current_process = next_process
            
        current_time += 1
        
    average_waiting_time = total_waiting_time / num_processes
    return completed_processes, average_waiting_time

def create_table(processes, average_waiting_time):
    # Print table header
    print("+-----+--------------+------------+----------+-----------------+----------------+--------------+")
    print("| PID | Arrival Time | Burst Time | Priority | Completion Time | Turnaround Time | Waiting Time |")
    print("+-----+--------------+------------+----------+-----------------+----------------+--------------+")
    
    for process in processes:
        print(f"| {process.pid:>3} | {process.arrival_time:>12} | {process.burst_time:>10} | {process.priority:>8} | "
              f"{process.completion_time:>15} | {process.turnaround_time:>14} | {process.waiting_time:>12} |")
    print("+-----+--------------+------------+----------+-----------------+----------------+--------------+")
    print(f"Average Waiting Time: {average_waiting_time}")

processes = [
    Process(1, 0, 5, 3),
    Process(2, 1, 2, 2),
    Process(3, 2, 1, 1),
    Process(4, 3, 4, 4),
    Process(5, 4, 3, 5)
]

completed_processes, average_waiting_time = sjf_preemptive(processes)

print("Completed Processes:")
for process in completed_processes:
    print(f"PID: {process.pid}, Arrival Time: {process.arrival_time}, Burst Time: {process.burst_time}, "
          f"Priority: {process.priority}, Completion Time: {process.completion_time}, "
          f"Turnaround Time: {process.turnaround_time}, Waiting Time: {process.waiting_time}")
print(f"Average Waiting Time: {average_waiting_time}")


# Output
# Completed Processes:
# PID: 3, Arrival Time: 2, Burst Time: 0, Priority: 1, Completion Time: 3, Turnaround Time: 1, Waiting Time: 1
# PID: 2, Arrival Time: 1, Burst Time: 0, Priority: 2, Completion Time: 4, Turnaround Time: 3, Waiting Time: 3
# PID: 5, Arrival Time: 4, Burst Time: 0, Priority: 5, Completion Time: 7, Turnaround Time: 3, Waiting Time: 3
# PID: 4, Arrival Time: 3, Burst Time: 0, Priority: 4, Completion Time: 11, Turnaround Time: 8, Waiting Time: 8
# PID: 1, Arrival Time: 0, Burst Time: 0, Priority: 3, Completion Time: 15, Turnaround Time: 15, Waiting Time: 15
# Average Waiting Time: 6.0
