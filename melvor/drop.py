from statistics import mean


class Drop:
    def __init__(self, name):
        self.name = name


class ItemDrop(Drop):
    def __init__(self, name, chance):
        super().__init__(name)
        self.chance = chance


class GoldDrop(Drop):
    def __init__(self, name, min_gp, max_gp):
        super().__init__(name)
        self.min_gp = min_gp
        self.max_gp = max_gp

    def avg_gp(self):
        return mean([self.min_gp, self.max_gp])

    def avg_gp_idle(self, idle_hrs):
        return self.avg_gp() * idle_hrs
