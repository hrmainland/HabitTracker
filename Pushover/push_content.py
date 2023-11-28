import requests
import json
from random import random, randint

API_KEY = "FTb/yxKhwxihKfjAvJSRVQ==kqDU9txtayI0PWSp"
INSULT_PROB = 1/4

LORD = [
    "tycoon",
    "magnate",
    "king",
    "prince",
    "baron",
    "czar",
    "lion",
    "monarch",
    "captain",
    "tsar",
    "star",
    "Napoleon",
    "mogul",
    "tzar",
    "god",
    "personage",
    "nawab",
    "nabob",
    "big boy",
    "big gun",
    "personality",
    "bigwig",
    "kahuna",
    "fat cat",
    "big wheel",
    "biggie",
    "notable",
    "honcho",
    "heavy",
    "big cheese",
    "deity",
    "main man",
    "celebrity",
    "supremo",
    "mover and shaker",
    "VIP",
    "superstar",
    "heavyweight",
    "bigfoot",
    "demigod",
    "big shot",
    "figure",
    "pooh-bah",
    "poo-bah",
    "tycoon",
    "magnate",
    "king",
    "prince",
    "baron",
    "czar",
    "lion",
    "monarch",
    "captain",
    "tsar",
    "star",
    "Napoleon",
    "mogul",
    "tzar",
    "god",
    "personage",
    "nawab",
    "nabob",
    "big boy",
    "big gun",
    "personality",
    "bigwig",
    "kahuna",
    "fat cat",
    "big wheel",
    "biggie",
    "notable",
    "honcho",
    "heavy",
    "big cheese",
    "deity",
    "main man",
    "celebrity",
    "supremo",
    "mover and shaker",
    "VIP",
    "superstar",
    "heavyweight",
    "bigfoot",
    "demigod",
    "big shot",
    "figure",
    "pooh-bah",
    "poo-bah"]
LOSER = [
    "half-pint",
    "subordinate",
    "lightweight",
    "underling",
    "nobody",
    "inferior",
    "nothing",
    "small-timer",
    "zero",
    "half-pint",
    "subordinate",
    "lightweight",
    "underling",
    "nobody",
    "inferior",
    "nothing",
    "small-timer",
    "zero"]


def capitalise_all(input):
    return " ".join([word.capitalize() for word in input.split(" ")])


def random_title():
    if random() > INSULT_PROB:
        return LORD[randint(0, len(LORD) - 1)]
    return LOSER[randint(0, len(LOSER) - 1)]


def random_lord_title():
    title = LORD[randint(0, len(LORD) - 1)]
    return capitalise_all(title)


def random_loser_title():
    title = LOSER[randint(0, len(LOSER) - 1)]
    return capitalise_all(title)


def success_quote():
    try:
        category = 'success'
        api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(
            category)
        response = requests.get(
            api_url, headers={'X-Api-Key': "FTb/yxKhwxihKfjAvJSRVQ==kqDU9txtayI0PWSp"})
        if response.status_code == requests.codes.ok:
            return json.loads(response.content)[0].get("quote")
        else:
            return "Come on Brother"
    except:
        return "Come on Brother"
