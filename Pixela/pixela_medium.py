import requests
import json
from datetime import date, timedelta

# Update these with your chosen token and username
TOKEN = "ExampleToken"
USERNAME = "mediumusername"

URL_BASE = "https://pixe.la"


# Decorator which retries an API call until successful
# (needed if not a Patreon supporter of Pixela)
def retry_decorator(func):
    def inner_function(*args):
        response = None
        while not response or (response.status_code != 200 and "isRejected\":true\"" in response.text):
            response = func(*args)
        content = json.loads(response.content)
        return content
    return inner_function


# Creates your account on Pixela
@retry_decorator
def create_user():
    data = f'{{"token":"{TOKEN}", "username":"{USERNAME}", "agreeTermsOfService":"yes", "notMinor":"yes"}}'
    response = requests.post('https://pixe.la/v1/users', data=data)
    return response

# Creates a Pixela graph
# (check the documentation for valid color codes)


@retry_decorator
def create_graph(name, id, unit, color_code, type="int"):
    url = f"{URL_BASE}/v1/users/{USERNAME}/graphs"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = f'{{"id":"{id}", "name":"{name}", "unit":"{unit}", "type":"int", "color":"{color_code}", "publishOptionalData":true}}'
    response = requests.post(url, headers=headers, data=data)
    return response


# Adds a datapoint to the specified graph for the specified day
@retry_decorator
def update_pixel(id, date, quantity):
    url = f"{URL_BASE}/v1/users/{USERNAME}/graphs/{id}/{date}"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    data = f'{{"quantity":"{quantity}"}}'
    response = requests.put(url, headers=headers, data=data)
    return response


# Returns the configuration of each graph associated with your account
@retry_decorator
def get_graph_definitions():
    url = f"{URL_BASE}/v1/users/{USERNAME}/graphs"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    response = requests.get(url, headers=headers)
    return response


TIME_FORMAT = "%Y%m%d"

# Returns the date 'past_days' ago in a time format accepted by Pixela
# eg. if past_days = 1, this will return yesterday's date formated


def past_date(past_days):
    return ((date.today() + timedelta(days=-past_days)).strftime(TIME_FORMAT))


# Returns data associated with the pixels (datapoints) for a given graph
@retry_decorator
def graph_pixels(id, days_captured):
    url = f"{URL_BASE}/v1/users/{USERNAME}/graphs/{id}/pixels"
    headers = {'X-USER-TOKEN': f'{TOKEN}'}
    from_date = past_date(days_captured)
    params = {"withBody": "true", "from": from_date}
    response = requests.get(url, headers=headers, params=params)
    return response


# ****************************************************************

# Parses input in the following format and updates specified graphs:
# {-past_days} {id_1} {quantity_1} {id_2} {quantity_2}...
# eg. an input of "-1 run 30 read 15" will add datapoints for yesterday
# to the graphs with ids "run" and "read" with quantities 30 and 15 respectively
def parse_input():
    day = date.today().strftime("%Y%m%d")
    user_input = input("Enter Datapoints:\n").split(" ")
    # for i, elem in enumerate(user_input):
    i = 0
    while i < len(user_input):
        if i == 0 and user_input[i][0] == "-":
            day = (date.today() +
                   timedelta(days=int(user_input[i]))).strftime("%Y%m%d")
            i += 1
            continue
        update_pixel(user_input[i], day, user_input[i + 1])
        print(f"{user_input[i]} datapoint added")
        i += 2


if __name__ == "__main__":
    # response = update_pixel("first", "20230724", "20")
    # print(get_graph_definitions())
    parse_input()

    print(graph_pixels("first", 7))
    # print("hey")
