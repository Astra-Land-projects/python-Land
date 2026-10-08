import json
from datetime import datetime

registry_file = "models.json"

try:

    with open(
        registry_file,
        encoding="utf-8"
    ) as f:

        registry = json.load(f)

except FileNotFoundError:

    registry = []


name = input("Model name: ")
version = input("Version: ")
path = input("Model path: ")
accuracy = float(
    input("Accuracy: ")
)

registry.append({
    "name": name,
    "version": version,
    "path": path,
    "accuracy": accuracy,
    "created": datetime.now().isoformat()
})

with open(
    registry_file,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        registry,
        f,
        indent=2
    )

print("Model registered.")