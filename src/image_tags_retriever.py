import json
import random
from typing import List
import requests
import shutil


def callapi(key: str = "22499447-34dc1e9873c70161efc9bd199") -> List[str]:
    """Generates a random image and some descriptors for the same

    :param key: a pixabay.com api access key
    :return: a list containing two elements - the url of a random image and a list of words describing the image
    """
    category = random.choice(
        [
            "backgrounds",
            "fashion",
            "nature",
            "science",
            "education",
            "feelings",
            "health",
            "people",
            "religion",
            "places",
            "animals",
            "industry",
            "computer",
            "food",
            "sports",
            "transportation",
            "travel",
            "buildings",
            "business",
            "music",
        ]
    )

    colors = random.sample(
        [
            "grayscale",
            "red",
            "orange",
            "yellow",
            "green",
            "turquoise",
            "blue",
            "lilac",
            "pink",
            "white",
            "gray",
            "black",
            "brown",
        ],
        k=random.randint(1, 14),
    )

    editors_choice = str(random.choice([True, False]))

    per_page = str(random.randint(3, 200))

    url = (
        "https://pixabay.com/api/?key={}&image_type=vector&per_page={}&editors_choice={}&category={}&colors="
        + "{}," * len(colors)
    ).format(key, per_page, editors_choice, category, *colors)

    apireturn = json.loads(requests.get(url).text)

    if apireturn["totalHits"]:
        imgaddress = apireturn["hits"][0]["webformatURL"]
        imgdescr = apireturn["hits"][0]["tags"].split(", ")
        return [imgaddress, imgdescr]
    else:
        return callapi()

def save_random_image() -> List[str]:
    """saves the generated image in a png file for ascii-conversion and returns the description"""
    link, desc = callapi()   
    path = "src/assets/image.png"    

    response = requests.get(link, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    return desc

