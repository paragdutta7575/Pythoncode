
def check_usage(cpu_check):

    Healthy = 0
    Unhealthy = 0

    for server_name, cpu in cpu_check.items():
       if cpu >= 80:
         Unhealthy += 1
         print (f"There is high CPU - testing")
       else :
         Healthy += 1
         print (f"All good - testing") 

cpu_check = {
    "web-1": 45,
    "web-2": 92,
    "web-3": 78,
    "web-4": 88,
    "db-1": 15,
    "db-2": 99,
    "cache-1": 60
}
check_usage(cpu_check)
