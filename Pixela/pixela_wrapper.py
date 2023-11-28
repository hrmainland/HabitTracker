from Pixela.api import *


def graph_def_to_id_dict(graphs_definition, attribute):
    # returns a dict of type {'id':'med', {attribute}:"value", ...}
    return {elem["id"]: elem[attribute] for elem in graphs_definition["graphs"]}


def streak(pixels, days_captured):
    # Returns a positive number for streak and a negative number for days missed
    # Doesn't include today (days_captured = 8, days checked will be 7)
    date_qty_dict = {elem["date"]: elem["quantity"] for elem in pixels}
    streak = None
    for past_days in range(1, days_captured):
        date = get_past_date(past_days)

        datapoint = date_qty_dict.get(date)
        positive_qty = datapoint and int(datapoint) != 0

        if past_days == 1:
            streak = positive_qty
            continue

        if streak != positive_qty:
            break
    if streak:
        return past_days - 1
    return -past_days + 1


# *******************************
# # Medium

# # Change the name of this
# from pixela_medium import *

# def streak(pixels, days_captured):
#     # Returns a positive number for streak and a negative number for days missed
#     # Doesn't include today (if days_captured = 8, days checked will be 7)
#     date_qty_dict = {elem["date"]: elem["quantity"] for elem in pixels}
#     streak = None
#     for past_days in range(1, days_captured):
#         date = past_date(past_days)

#         # determine if there is a positive quantity associated with the day
#         datapoint = date_qty_dict.get(date)
#         positive_qty = datapoint and int(datapoint) > 0

#         # establish if this is a streak or missed days based on yesterday's result
#         if past_days == 1:
#             streak = positive_qty
#             continue

#         # break when the streak ends
#         if streak != positive_qty:
#             break

#     # return (positive/negative) number of days for (streak/missed days)
#     if streak:
#         return past_days - 1
#     return -past_days + 1
