#!/usr/bin/env python

# ('Dusty Oak Staff', {'Health': 9, 'Energy': 14, 'Strength': 15, 'Defense': 9, 'Type': 'Dusty', 'Worth': 4})
# ('Forsaken Chestplate', {'Health': 6524, 'Energy': 247872, 'Strength': 206, 'Defense': 29, 'Type': 'Forsaken', 'Worth': 32})
# ('Shiny Legs', {'Health': 497, 'Energy': 255, 'Strength': 105, 'Defense': 24, 'Type': 'Shiny', 'Worth': 13})

# ####

# def equip(self, game_item):
#         self._game_item = game_item
#         for key, value in self._game_item.items():
#             self._equipment.setdefault(key, value)
#             for key, value in value.items():
#                 if key == 'Strength':
#                     self._strength_weapon += value
#                     self._fight_strength += value
#                 if key == 'Health':
#                     self._health_weapon += value
#                     self._fight_health += value
#                 if key == 'Energy':
#                     self._energy_weapon += value
#                     self._fight_energy += value
#                 if key == 'Defense':
#                     self._defense_weapon += value
#                     self._fight_defense += value

# def remove_item(self, game_item):
#         self._game_item = game_item
#         for item_key, value in self._game_item.items():
#             for key, value in value.items():
#                 if key == 'Strength':
#                     self._strength_weapon -= value
#                     self._fight_strength -= value
#                 if key == 'Health':
#                     self._health_weapon -= value
#                     self._fight_health -= value
#                 if key == 'Energy':
#                     self._energy_weapon -= value
#                     self._fight_energy -= value
#                 if key == 'Defense':
#                     self._defense_weapon -= value
#                     self._fight_defense -= value

game_items = {
    'Dusty Oak Staff': {'type': 'Dusty', 'modifiers': (9, 14, 15, 9, 4)},
    'Forsaken Chestplate': {'type': 'Forsaken', 'modifiers': (6524, 247872, 206, 29, 32)},
    'Shiny Legs': {'type': 'Shiny', 'modifiers': (497, 255, 105, 24, 13)},
}

class Player(object):

    def __init__(self, *args, **kwargs):
        self.health = kwargs.get('health', 20)
        self.energy = kwargs.get('energy', 20)
        self.strength = kwargs.get('strength', 20)
        self.defense = kwargs.get('defense', 20)
        self.worth = kwargs.get('worth', 20)
        self.inventory = {}

    def __str__(self):
        stats = 'Stats\n=====\n'
        stats += '{:<10}: {:>10}\n'.format('Health', self.health)
        stats += '{:<10}: {:>10}\n'.format('Energy', self.energy)
        stats += '{:<10}: {:>10}\n'.format('Strength', self.strength)
        stats += '{:<10}: {:>10}\n'.format('Defense', self.defense)
        stats += '{:<10}: {:>10}\n\n'.format('Worth', self.worth)
        if self.inventory:
          stats += 'Inventory\n=========\n'
          for item in self.inventory:
              stats += item
        stats += '\n'
        return stats

    def equip(self, item, attributes):
        if item not in self.inventory:
            self.inventory[item] = attributes
            self.health += attributes[0]
            self.energy += attributes[1]
            self.strength += attributes[2]
            self.defense += attributes[3]
            self.worth += attributes[4]

    def drop(self, item, attributes):
        if item in self.inventory:
            del self.inventory[item]
            self.health -= attributes[0]
            self.energy -= attributes[1]
            self.strength -= attributes[2]
            self.defense -= attributes[3]
            self.worth -= attributes[4]

player = Player(health=50, worth=100)
print(player)
item = 'Shiny Legs'
player.equip(item, game_items.get(item, {}).get('modifiers'))
print(player)
player.drop(item, game_items.get(item, {}).get('modifiers'))
print(player)

