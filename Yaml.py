
import yaml

data = {
    "server": "cache-1",
    "cpu": 30,
    "status": "healthy"
}

with open("output.yaml","w") as f:
    yaml.dump(data, f, indent=4)