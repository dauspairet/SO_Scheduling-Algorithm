class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.wait_time = 0
        self.status = "NEW"  # five status states: NEW, READY, RUNNING, WAITING, TERMINATED
    
    def __str__(self):
        return f"{self.name} ({self.arrival_time}, {self.burst_time}, {self.wait_time}) [{self.status}]"

class Scheduler:
    def __init__(self, processes):
        self.processes = processes
        self.time = 0
    
    def next_process(self):
        # find the next process to be executed
        for process in self.processes:
            if process.status == "NEW":
                process.status = "READY"
            
            if process.status == "READY":
                return process
        
        return None
    
    def run(self):
        # run the processes in FIFO order
        while True:
            next_process = self.next_process()
            if next_process is None:
                print("All processes executed")
                break
            
            # mark the process as running and update its wait time
            next_process.status = "RUNNING"
            next_process.wait_time += self.time - next_process.arrival_time
            
            # execute the process for its burst time
            self.time += next_process.burst_time
            
            print(next_process)
            
            next_process.status = "TERMINATED"
            
            # update the status of other processes that are waiting
            for process in self.processes:
                if process.status == "READY":
                    process.status = "WAITING"
                elif process.status == "WAITING":
                    process.wait_time += next_process.burst_time
                
            print(next_process)

# create some processes
p1 = Process("P1", 0, 4)
p2 = Process("P2", 1, 3)
p3 = Process("P3", 2, 4)
p4 = Process("P4", 3, 6)

# create a scheduler and run the processes
scheduler = Scheduler([p1, p2, p3, p4])
scheduler.run()

# Output
# P1 (0, 4, 0) [RUNNING]
# P1 (0, 4, 0) [TERMINATED]
# P2 (1, 3, 3) [RUNNING]
# P2 (1, 3, 3) [TERMINATED]
# P3 (2, 4, 5) [RUNNING]
# P3 (2, 4, 5) [TERMINATED]
# P4 (3, 6, 8) [RUNNING]
# P4 (3, 6, 8) [TERMINATED]
# All processes executed
