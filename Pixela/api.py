import requests
from datetime import date, timedelta
from ast import literal_eval
import json


URL_BASE = "https://pixe.la"

OLD_USERNAME = "hrmainland"
OLD_TOKEN = "Parkour99"

USERNAME = "hmainland"
TOKEN = "bigoldtoken"

TIME_FORMAT = "%Y%m%d"

# Just type this in with the correct values to see your graph
# https://pixe.la/v1/users/hmainland/graphs/med?mode=short
# or use this to see the habit page
# https://pixe.la/v1/users/hmainland/graphs/med.html

# home page
# https://pixe.la/@hmainland


def convert_color(color):
    # Converts plain english color to string accepted by API
    color_dict = {"green": "shibafu", "red": "momiji", "blue": "sora",
                  "yellow": "ichou", "purple": "ajisai", "black": "kuro"}
    return (color_dict[color.lower()])


def decode_bytes(input):
    string = input.decode('utf-8')
    string = string.replace("null", "None")
    string = string.replace("false", "False")
    string = string.replace("true", "True")
    return (literal_eval(string))


def get_past_date(past_days):
    return ((date.today() + timedelta(days=-past_days)).strftime(TIME_FORMAT))


def create_user():
    data = '{"token":"bigoldtoken", "username":"hmainland", "agreeTermsOfService":"yes", "notMinor":"yes", "thanks-code":"e7c8d63a5fd285e8f86fa0c9f82157db577e7ae62ea5e724c5273030a33b27c5"}'
    response = requests.post('https://pixe.la/v1/users', data=data)
    pass
    print(response.content)

# Jeff8080


def upgrade_account():
    # doesn't work
    url = "https://pixe.la/v1/users/hmainland"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = '{"newToken":"bigoldtoken", "thanksCode":"e7c8d63a5fd285e8f86fa0c9f82157db577e7ae62ea5e724c5273030a33b27c5"}'
    response = requests.put(url, headers=headers, data=data)
    pass
    print(response.content)


def update_profile(**kwargs):
    url = "https://pixe.la/@hmainland"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = ""
    i = 0
    for key, value in kwargs.items():
        if i:
            data += ","
        data += f"\"{key}\":\"{value}\""
        i += 1
    data = "{" + data + "}"
    response = requests.put(url, headers=headers, data=data)
    print(response.content)


def add_graph(name, id, unit, color, type="int"):
    color_code = convert_color(color)
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = f'{{"id":"{id}", "name":"{name}", "unit":"{unit}", "type":"int", "color":"{color_code}", "publishOptionalData":true}}'
    response = requests.post(url, headers=headers, data=data)
    pass
    print(response.content)


def update_pixel(id, date, quantity):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}/{date}"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = f'{{"quantity":"{quantity}"}}'
    response = requests.put(url, headers=headers, data=data)
    print(response.content)


def update_graph(id, **kwargs):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = ""
    i = 0
    for key, value in kwargs.items():
        if i:
            data += ","
        data += f"\"{key}\":\"{value}\""
        i += 1
    data = "{" + data + "}"
    response = requests.put(url, headers=headers, data=data)
    pass
    print(response.content)


def delete_graph(id):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    response = requests.delete(url, headers=headers)
    print(response.content)


def graph_svg(id, mode="short"):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}"
    print(url)
    params = f'{{"mode":"{mode}"}}'
    response = requests.get(url, params=params)
    pass
    print(response.content)


def test():
    response = requests.get(
        "https://pixe.la/v1/users/hrmainland/graphs/meditate", params={"mode": "short"})
    pass
    print(response)


def get_stats(id):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}/stats"
    print(url)
    response = requests.get(url)
    return json.loads(response.content)


def get_graph_definition(id):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}/graph-def"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    response = requests.get(url, headers=headers)
    return (decode_bytes(response.content))


def get_graph_definitions():
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    response = requests.get(url, headers=headers)
    pass
    return (decode_bytes(response.content))


def all_ids():
    return [elem["id"] for elem in get_graph_definitions()["graphs"]]


def get_all_attribute(attribute):
    # Get a list of all the given attribute accross all graphs. ie. id, name unit
    return [elem[attribute] for elem in get_graph_definitions()["graphs"]]


def get_pixel(id, date):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}/{date}"
    print(url)
    # return
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    response = requests.get(url, headers=headers)
    pass
    print(response.content)


def get_graph_pixels(id, days_captured, past_days=0):
    # Returns dates and quantities for a given graph
    # days_captured is inclusive of today as a day
    # (ie. today = 28, days_captured = 3, days_captured = 26 for 3 days)
    # use past_days to end the reporting period n days in the past
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}/pixels"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    from_date = get_past_date(days_captured - 1 + past_days)
    to_date = get_past_date(past_days)
    params = {"withBody": "true", "to": to_date, "from": from_date}
    response = requests.get(url, headers=headers, params=params)
    return decode_bytes(response.content)


def get_all_counts(days_captured, past_days=0):
    counts = {}
    ids = all_ids()
    for id in ids:
        positive_count = 0
        graph_pixels = get_graph_pixels(
            id, days_captured, past_days)['pixels']
        for entry in graph_pixels:
            if int(entry["quantity"]) > 0:
                positive_count += 1
        counts[id] = positive_count
        # counts[id] = len(get_graph_pixels(
        #     id, days_captured, past_days)['pixels'])
    return counts


def add_datapoint(id, quantity=1, date=date.today().strftime("%Y%m%d")):
    url = URL_BASE + f"/v1/users/{USERNAME}/graphs/{id}"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = f'{{"quantity":"{quantity}", "date":"{date}"}}'
    response = requests.post(url, headers=headers, data=data)
    if int(response.status_code) == 200:
        print(id, "datapoint added")
    else:
        print(response.content)


def for_all_graphs(func):
    # pass in a function which acts on a single graph and this will make it act on all
    for id in get_all_attribute("id"):
        func()


if __name__ == "__main__":
    pass
    add_graph("Sleep", "sleep", 10, "blue")
