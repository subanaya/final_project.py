# class for characters
class Character():
    def __init__(self, name, adjecive, skill, health_points):
        self.name = name
        self.adjective = adjecive
        self.skill = skill
        self.health_points = health_points

    def __str__(self):
        description = f"""
{self.name} is {self.adjective}.
{self.name}'s skill is {self.skill}.
{self.name} has {self.health_points}.
        """
        return description


# class for the characters' inventories
class Inventory():
    def __init__(
        self, character_name, weapon_1, weapon_2,
        weapon_1_description, weapon_1_damage, weapon_1_healing,
        weapon_2_description, weapon_2_damage, weapon_2_healing
                ):
        self.character_name = character_name
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2
        self.weapon_1_description = weapon_1_description
        self.weapon_1_damage = weapon_1_damage
        self.weapon_1_healing = weapon_1_healing
        self.weapon_2_description = weapon_2_description
        self.weapon_2_damage = weapon_2_damage
        self.weapon_2_healing = weapon_2_healing

    def __str__(self):
        description = f"""

{self.character_name}'s Inventory:
* {self.weapon_1}
Description: {self.weapon_1_description}
Damage: {self.weapon_1_damage}
Healing: {self.weapon_1_healing}
\n
* {self.weapon_2}
Description: {self.weapon_2_description}
Damage: {self.weapon_2_damage}
Healing: {self.weapon_2_healing}
      """
        return description
