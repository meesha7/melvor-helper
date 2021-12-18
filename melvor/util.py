from math import log


def gacha(drop_chance, attempts):
    return 100 * (1 - (1 - drop_chance / 100) ** attempts)


def reverse_gacha(drop_chance, p=99):
    return log(1 - p / 100) / log(1 - drop_chance / 100)


def format_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return f"{hour:.0f}h {minutes:.0f}m"


def num_actions(idle_hrs, action_time):
    return idle_hrs * 3600 / action_time
