import psutil

# Define threshold values
cpu_threshold = 80
memory_threshold = 80
disk_threshold = 80

# Get system metrics
cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent
running_processes = len(psutil.process_iter())

# Check and alert if thresholds are exceeded
if cpu_usage > cpu_threshold or memory_usage > memory_threshold or disk_usage > disk_threshold:
    alert_message = f"System Alert: CPU({cpu_usage}%) Memory({memory_usage}%) Disk({disk_usage}%)\n"
    with open('system_alert.log', 'a') as log_file:
        log_file.write(alert_message)
    print(alert_message)
else:
    print("System is healthy.")

#  Log running processes
with open('running_processes.log', 'a') as processes_log:
    processes_log.write(f"Running Processes: {running_processes}\n")
