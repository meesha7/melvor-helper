import enum
from statistics import mean

from melvor import util


class DamageType(enum.Enum):
    MELEE = 1
    RANGED = 2
    MAGIC = 3


class Attack:
    def __init__(self, min_hit, max_hit, chance):
        self.min_hit = min_hit
        self.max_hit = max_hit
        self.chance = chance


class Player:
    def __init__(self, dmg_type, dr):
        self.dmg_type = dmg_type
        self.dr = dr


class Monster:
    def __init__(self, dmg_type, attack_speed, hit_chance):
        self.dmg_type = dmg_type
        self.attack_speed = attack_speed
        self.hit_chance = hit_chance
        self.attacks = []

    def add_attack(self, attack):
        self.attacks.append(attack)

    @classmethod
    def load(cls, name):
        resource = util.load_resource("monsters.yaml")
        data = resource[name]

        return cls(**data)


class Combat:
    def __init__(self, player, monster, auto_eat):
        self.player = player
        self.monster = monster
        self.auto_eat = auto_eat

    def damage_type_dr_mod(self):
        DR_MOD_TABLE = {
            DamageType.MELEE: {
                DamageType.MELEE: 1.0,
                DamageType.RANGED: 1.25,
                DamageType.MAGIC: 0.5,
            },
            DamageType.RANGED: {
                DamageType.MELEE: 0.95,
                DamageType.RANGED: 1.0,
                DamageType.MAGIC: 1.25,
            },
            DamageType.MAGIC: {
                DamageType.MELEE: 1.25,
                DamageType.RANGED: 0.85,
                DamageType.MAGIC: 1.0,
            },
        }

        return DR_MOD_TABLE[self.player.dmg_type][self.monster.dmg_type]

    def avg_dmg_per_hit(self):
        dmg_per_hit = 0

        for attack in self.monster.attacks:
            avg_hit_dmg = mean([attack.min_hit, attack.max_hit])
            dmg_per_hit += avg_hit_dmg * (attack.chance / 100)

        return dmg_per_hit

    def avg_dmg_idle(self, idle_hrs):
        hits = util.num_actions(idle_hrs, self.monster.attack_speed) * (
            self.monster.hit_chance / 100
        )

        return hits * self.avg_dmg_per_hit()

    def req_food_count_max(self, idle_hrs):
        return self.avg_dmg_idle(idle_hrs) / self.auto_eat.one_heal()

    def hits_before_empty_avg(self):
        return self.auto_eat.max_heal() / self.avg_dmg_per_hit()

    def max_idle_time_avg(self):
        return (
            self.hits_before_empty_avg()
            * self.monster.attack_speed
            / (self.monster.hit_chance / 100)
        )
