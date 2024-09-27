import pandas as pd

class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin_scheduling(processes, time_quantum):
    time = 0
    completed = 0
    queue = []
    n = len(processes)
    process_order = []  # New list to keep track of process order
    
    while completed < n:
        for process in processes:
            if process.arrival_time <= time and process.remaining_time > 0 and process not in queue:
                queue.append(process)
        
        if not queue:
            time += 1
            continue
        
        current_process = queue.pop(0)
        process_order.append(current_process.pid)  # Add PID to process order
        
        if current_process.remaining_time <= time_quantum:
            time += current_process.remaining_time
            current_process.remaining_time = 0
        else:
            time += time_quantum
            current_process.remaining_time -= time_quantum
        
        if current_process.remaining_time > 0:
            queue.append(current_process)
        else:
            completed += 1
            current_process.completion_time = time
            current_process.turnaround_time = current_process.completion_time - current_process.arrival_time
            current_process.waiting_time = current_process.turnaround_time - current_process.burst_time
    
    return processes, process_order  # Return both completed processes and process order


df = pd.read_excel('/Users/abhijit/AllProjects/AI-industry-4.0/Assignments/Assignment9/process_data.xlsx')
processes = [Process(row['PID'], row['Arrival Time'], row['Burst Time'], row['Priority']) 
                 for _, row in df.iterrows()]
    
    
time_quantum = 2
    
    
completed_processes, process_order = round_robin_scheduling(processes, time_quantum)
    
    
print("PID\tArrival Time\tBurst Time\tPriority\tCompletion Time\tTurnaround Time\tWaiting Time")
for process in completed_processes:
    print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.priority}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")
    
    # Print process order
print("\nProcess execution order:")
print(" -> ".join(map(str, process_order)))
