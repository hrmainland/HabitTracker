from Pixela.api import add_datapoint, get_graph_definitions
import sys
from datetime import date, timedelta
# from Pixela.file_io import *

UNIT_DICT = {"med": 30, "jrn": 10, "sleep": 10, "web": 30, "ex": 45}

DAY_STRINGS = {"yest": -1, "yesterday": -1, "tod": 0, "today": 0}


# example input
# -2 med 3 run yesterday med read 2 tod run
# This means
# Two days ago: meditated 3 sessions, ran once
# Yesterday: meditated and read once each
# Today ran one time

# or
# read 2 run
# Today: read 2 sessions, ran once

class Datapoint:
    # Datapoint to be added. Default of 1 unit today.
    def __init__(self, id, unit_dict) -> None:
        self.id = id
        self.date = date.today().strftime("%Y%m%d")
        self.quantity = unit_dict[self.id]

    def __str__(self):
        return (f"Datapoint:\nid: {self.id}\ndate:{self.date}\nquantity:{self.quantity}")

    # def set_default_quantity(self, unit_dict):
    #     self.quantity =


def get_name_id_pairs(graph_definitions):
    name_id_pairs = {}
    for elem in graph_definitions["graphs"]:
        name_id_pairs[elem["id"]] = elem["name"]
    return name_id_pairs


def prompt_user(name_id_pairs):
    print("""\nInput the day (ie, "tod" or -2 (two days ago)) followed by the graph id and the quantity.
    Default quantity is stored locally. If all have been done today, no need for the day indicator.
    \neg. -2 med 3 run yesterday med read 2 tod run
    or simply: read 2 run\n\n***********\n""")
    print("The current Names and IDs are:\n")
    for id, name in name_id_pairs.items():
        print(f"{name:<16}\t{id}")
    print("\n")


def parse_input(input, id_list):

    # file = File(UNIT_FILE)

    if len(input) == 0:
        print("No Input Received")
        return None

    datapoints = []
    current_datapoint = None

    if input[0] == "all":
        for id in id_list:
            this_datapoint = Datapoint(id, UNIT_DICT)
            datapoints.append(this_datapoint)
        return datapoints

    # if there's no day indicator we're talking about today
    day = date.today().strftime("%Y%m%d")
    for i, elem in enumerate(input):
        if elem[0] == "-":
            # no need to assert that the rest of the string is a number
            # terminal won't recopgnise a dash followed by letters
            day = (date.today() + timedelta(days=int(elem))).strftime("%Y%m%d")
            continue
        elif elem in DAY_STRINGS:
            # if written in words ("yest", "today")
            day = (date.today() +
                   timedelta(days=DAY_STRINGS[elem])).strftime("%Y%m%d")
            continue

        # now to parse the id and quantity
        if elem in id_list:
            # first add the last datapoint you were working on
            if current_datapoint:
                datapoints.append(current_datapoint)

            # now make a new datapoint
            current_datapoint = Datapoint(elem, UNIT_DICT)
            current_datapoint.date = day
        else:
            try:
                current_datapoint.quantity = int(elem)
            except:
                print(
                    f"Expecting a quantity in position {i + 1} instead of {elem}.")

    # add last element
    datapoints.append(current_datapoint)
    return datapoints

# input format
# yesterday web 10 job 20
# web 15 job 20
# -3 web 20 job 45
# split
# pull out front value (defined value or negative)
# add pairs of values directly


def main():
    graph_definitions = get_graph_definitions()
    name_id_pairs = get_name_id_pairs(graph_definitions)
    if len(sys.argv) > 1:
        datapoint_code = sys.argv[1:]
    else:
        prompt_user(name_id_pairs)
        datapoint_code = input("Enter datapoints:\n").split(" ")
    datapoints = parse_input(datapoint_code, list(
        set(name_id_pairs.keys()).intersection(set(UNIT_DICT.keys()))))

    # for datapoint in datapoints:
    #     print(datapoint)
    #     print('\n')
    for datapoint in datapoints:
        add_datapoint(datapoint.id, datapoint.quantity, datapoint.date)


if __name__ == "__main__":
    main()
