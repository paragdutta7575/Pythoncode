
import re

with open ("Logs.log") as f:
     for line in f:
        match = re.search(r"\w+\.\w+\.\w+\.\w+", line)
        if match:
            print("Found Error", match.group())