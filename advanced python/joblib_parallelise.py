import math
import time
from joblib import Parallel,delayed
from colorthief import ColorThief
import os
import uuid
import pandas as pd
import requests

t1 = time.time()

#results = [math.factorial(x) for x in range(10000)]
#results = Parallel(n_jobs=8)(delayed(math.factorial)(x) for x in range(10000))

t2 = time.time()

print(t2-t1)

data = pd.read_csv("dress.csv")


def extract_image_colors(url):
    unique_id = uuid.uuid4()
    with open(f"{unique_id}.jpg","wb") as f:
        f.write(requests.get(url).content)

    color_thief = ColorThief(f"{unique_id}.jpg")
    palette = color_thief.get_palette(color_count=2)
    os.remove(f"{unique_id}.jpg")
    return palette[0],palette[1]


colors = []

t1 = time.time()

for url in data['image_url'].values[:100]:
    colors.append(extract_image_colors(url))

t2 = time.time()

print(t2 - t1)


t1 = time.time()

colors2 = Parallel(n_jobs=-1)(delayed(extract_image_colors)(url) for url in data['image_url'].values[:100])

t2 = time.time()

print(t2 - t1)

# without parallel : 158.30930924415588 s
# with parallel    : 18.6430447101593 s



