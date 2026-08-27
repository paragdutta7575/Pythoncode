
import json
import re

#Load alert config
with open("alert_config.json") as f:
    config = json.load(f)

# scan logs
with open (Logs.log) as f:
    for line in f:
        #check for error keywords
        for keyword in config ["error_keywords"]:
            if keyword in line:
                print(f"ALERT : Found {keyword} =>")    
