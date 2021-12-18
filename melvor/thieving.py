from statistics import mean

from melvor import util
from melvor.drop import GoldDrop, ItemDrop


class ThievingTarget:
    def __init__(self, max_hit, action_time, chance):
        self.max_hit = max_hit
        self.action_time = action_time
        self.chance = chance
        self.stun_chance = 100 - self.chance
        self.drops = []

    def add_drop(self, drop):
        self.drops.append(drop)

    def max_dmg_idle(self, idle_hrs):
        hits = util.num_actions(idle_hrs, self.action_time) * (self.stun_chance / 100)

        return hits * self.max_hit

    def avg_dmg_idle(self, idle_hrs):
        hits = util.num_actions(idle_hrs, self.action_time) * (self.stun_chance / 100)

        return hits * mean([0, self.max_hit])

    def req_food_count_max(self, idle_hrs, auto_eat):
        return self.avg_dmg_idle(idle_hrs) / auto_eat.one_heal()

    def hits_before_empty_max(self, auto_eat):
        return auto_eat.max_heal() / self.max_hit

    def hits_before_empty_avg(self, auto_eat):
        return auto_eat.max_heal() / mean([0, self.max_hit])

    def max_idle_time_max(self, auto_eat):
        return (
            self.hits_before_empty_max(auto_eat)
            * self.action_time
            / (self.stun_chance / 100)
        )

    def max_idle_time_avg(self, auto_eat):
        return (
            self.hits_before_empty_avg(auto_eat)
            * self.action_time
            / (self.stun_chance / 100)
        )

    def gp_stolen_idle(self, idle_hrs):
        num_actions = util.num_actions(idle_hrs, self.action_time)
        total = 0

        for drop in self.drops:
            if isinstance(drop, GoldDrop):
                total += drop.avg_gp() * num_actions

        return total

    def item_drop_chances_idle(self, idle_hrs):
        num_actions = util.num_actions(idle_hrs, self.action_time)
        table = []

        for drop in self.drops:
            if isinstance(drop, ItemDrop):
                table.append([drop.name, util.gacha(drop.chance, num_actions)])

        return table
