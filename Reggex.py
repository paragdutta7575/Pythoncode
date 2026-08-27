
import re

log_data = """
Error from 192.168.1.10
Warning from 10.0.0.5
Connection reset by 172.16.0.2
"""

find_ip = re.findall(r"\d+\.\d+\.\d+\.\d+", log_data)
print(find_ip)