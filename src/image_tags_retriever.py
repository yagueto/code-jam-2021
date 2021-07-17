import json
import random
from typing import List

import requests


def callapi(key: str = "22499447-34dc1e9873c70161efc9bd199") -> List:
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
            "transparent",
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
        callapi()


if __name__ == "__main__":
    callapi()
