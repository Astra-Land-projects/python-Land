from PIL import Image
import numpy as np
from pathlib import Path

def vector(path):

    image = Image.open(
        path
    ).convert("RGB")

    image = image.resize(
        (32, 32)
    )

    return np.array(
        image,
        dtype=float
    ).flatten()


folder = Path("images")

files = list(
    folder.glob("*.jpg")
)

vectors = {
    file: vector(file)
    for file in files
}

query = Path(
    input("Query image: ")
)

q = vector(query)

results = []

for file, v in vectors.items():

    distance = np.linalg.norm(
        q - v
    )

    results.append(
        (distance, file)
    )

for distance, file in sorted(results)[:5]:

    print(
        file,
        "distance:",
        round(distance, 2)
    )