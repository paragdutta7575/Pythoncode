
#age = 301
#Name = "Parag"

#Message = f"Hi {Name} your age is {age}"
#print(Message)


#def CPU_check(CPU_usage):
    #for value in CPU_usage:
        #if value >= 80:
           #print (f"High CPU consumption")

#CPU_usage = [45, 92, 78, 88, 15, 99, 60]
#CPU_check(CPU_usage)

def check_pod(pod_usage):
      healthy = 0
      unhealthy = 0

      for value in pod_usage:
        if value >= 80:
           print ("High pod usage")
           unhealthy += 1
        elif value >= 60 :
           print ("growing pod usage")
           unhealthy += 1
        else :
           print ("All good")
           healthy += 1

pod_usage = [45, 92, 78, 88, 15, 99, 60]           
check_pod(pod_usage)
