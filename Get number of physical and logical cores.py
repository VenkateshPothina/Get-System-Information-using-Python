import psutil

print(f"Number of physical cores: {psutil.cpu_count(logical=False)}")
print(f"Number of logical cores: {psutil.cpu_count(logical=True)}")

print(f"Current CPU frquency: {psutil.cpu_freq().current}")
print(f"Min CPU frequency: {psutil.cpu_freq().min}")
print(f"Min CPU frequency: {psutil.cpu_freq().max}")

print(f"Current CPU utilization: {psutil.cpu_percent(interval=1)}")
print(f"Current per-CPU utilization: {psutil.cpu_percent(interval=1,percpu=True)}")

