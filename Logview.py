
def review_logs():
    with open("Logs.log", "r") as f:
     for line in f:
        if "ERROR" in line:
            print(line)

review_logs()