from queue import PriorityQueue

class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = None
        self.turnaround_time = None
        self.waiting_time = None

    def __lt__(self, other):
        return self.remaining_time < other.remaining_time

def sjn_preemptive(processes):
    ready_queue = PriorityQueue()
    current_time = 0
    num_processes = len(processes)
    completed_processes = []
    current_process = None
    total_waiting_time = 0

    while len(completed_processes) < num_processes:
        for process in processes:
            if process.arrival_time == current_time:
                ready_queue.put(process)

        if current_process is not None and (current_process.remaining_time == 0 or (not ready_queue.empty() and current_process.remaining_time > ready_queue.queue[0].remaining_time)):
            ready_queue.put(current_process)
            current_process = None

        if ready_queue.empty():
            current_time += 1
            continue

        next_process = ready_queue.get()
        next_process.remaining_time -= 1

        if next_process.remaining_time == 0:
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
    print("+-----+--------------+------------+-----------------+----------------+--------------+")
    print("| PID | Arrival Time | Burst Time | Completion Time | Turnaround Time | Waiting Time |")
    print("+-----+--------------+------------+-----------------+----------------+--------------+")

    for process in processes:
        print(f"| {process.pid:>3} | {process.arrival_time:>12} | {process.burst_time:>10} | "
              f"{process.completion_time:>15} | {process.turnaround_time:>14} | {process.waiting_time:>12} |")
    print("+-----+--------------+------------+-----------------+----------------+--------------+")
    print(f"Average Waiting Time: {average_waiting_time}")

processes = [
    Process(1, 0, 5),
    Process(2, 1, 2),
    Process(3, 2, 1),
    Process(4, 3, 4),
    Process(5, 4, 3)
]

completed_processes, average_waiting_time = sjn_preemptive(processes)

# Call create_table function to print the table
create_table(completed_processes, average_waiting_time)

print("Completed Processes:")
for process in completed_processes:
    print(f"PID: {process.pid}, Arrival Time: {process.arrival_time}, Burst Time: {process.burst_time}, "
          f"Completion Time: {process.completion_time}, Turnaround Time: {process.turnaround_time}, "
          f"Waiting Time: {process.waiting_time}")
print(f"Average Waiting Time: {average_waiting_time}")
