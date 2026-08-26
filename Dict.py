def cpu_check(server_cpu):
    healthy = 0
    unhealthy = 0

    for server_name, cpu in server_cpu.items():
        if cpu >= 80:
            unhealthy += 1
            print(server_name, cpu, "ALMOST CRASHING")
        elif cpu >= 60:
           print (server_name, cpu, "WARNING")
           unhealthy += 1
        else :
           print ("All good", server_name, cpu,)
           healthy = 0
 
server_cpu = {
    "web-1": 45,
    "web-2": 92,
    "web-3": 78,
    "web-4": 88,
    "db-1": 15,
    "db-2": 99,
    "cache-1": 60
}

cpu_check(server_cpu)

    
