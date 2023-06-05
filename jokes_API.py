import requests


def joke_catch():
    joke = {"id": "",
            "joke": ""}
    r = requests.get("https://api.chucknorris.io/jokes/random")
    if r:
        response = r.json()
        joke = {"id": response["id"],
                "joke": response["value"]}
    return joke

