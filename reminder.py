# The idea is to check for any tasks not completed for x days and send a reminder to my phone to do them

# Steps
# - Use cron to run script every day
# - For each graph
#     - Retrieve unit from file
#     - Check last x days
#     - if 0 out of the last x days have a quanity above unit
#         - if no positive datapoints:
#             - send one push
#         - else
#             - send more mild push

from Pixela.pixela_wrapper import *
from Pixela.file_io import *
from Pixela.api import *
from Pushover.push_content import *
from Pushover.pushover_api import *
from random import randint

# How many days in the past are we looking
LOOK_BEHIND_DAYS = 365
# how many days of 0 before sending out a reminder
REMINDER_DAYS = 2
# When to send out a streak congrats message
MILESTONES = {
    7: "one week", 
    14: "two weeks", 
    30: "one month",
    61: "two months",
    92: "three months(!)"
}

def generate_title(is_streak: bool, days: int, name: str) -> str:
    if is_streak:
        return f"{random_lord_title()}, {days} day streak for {name}. Nice."
    return f"Oi {random_loser_title()}, {days} missed days for {name}."


def remind_all():
    unit_file = File(UNIT_FILE)
    id_name_dict = graph_def_to_id_dict(get_graph_definitions(), "name")

    # manual filter - there's a better way to do this
    all_ids = list(unit_file.df.index)
    account_ids = []
    account_bools = list(unit_file.df.account)
    for i in range(len(all_ids)):
        if account_bools[i]:
            account_ids.append(all_ids[i])

    for id in account_ids:
        streak_days = streak(get_graph_pixels(id, LOOK_BEHIND_DAYS)[
                             "pixels"], LOOK_BEHIND_DAYS)
        is_streak = streak_days > 0
        if not is_streak:
            if abs(streak_days) < REMINDER_DAYS:
                continue
        else:
            if streak_days not in MILESTONES:
                continue
        title = generate_title(is_streak, abs(streak_days), id_name_dict[id])
        send_push(title, success_quote())


def sample_push():
    task = ["Meditate", "Read", "Exercise", "Web Dev"][randint(0, 3)]
    name = " ".join([word.capitalize() for word in random_title().split(" ")])
    title = f"Time to {task} {name}"
    message = success_quote()
    send_push(title, message)


sample_push()
# remind_all()
