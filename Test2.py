from collections import Counter

def CPU_Check(cpu_usage):
    for value in cpu_usage:
        if value >= 80 :
            print (f"warning")
        else :
            print (f"none")

cpu_usage = [45, 92, 78, 88, 15, 99, 60]    
cnt = Counter        
CPU_Check(cpu_usage)