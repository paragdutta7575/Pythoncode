
def get_server_status(server_cpu, name):

    for server_cpu, cpu in server_cpu.items():
        if cpu >= 80 :
         print (server_cpu, cpu, "CRASHING")
        elif :    
         pass
        else :
         print ("ALL GOOD")
        
server_cpu = {
    "web-1": 45,
    "web-2": 92,
    "web-3": 78,
    "web-4": 88,
    "db-1": 15,
    "db-2": 99,
    "cache-1": 60
}

get_server_status(server_cpu, "web-1")
get_server_status(server_cpu, "web-99")