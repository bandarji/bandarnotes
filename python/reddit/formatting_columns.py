weapons = {
    'bandits dagger': {'weight': 0.5, 'attack': 56 },
    'bastard sword': {'weight': 6.0, 'attack': 105},
    'crescent axe': {'weight': 7.0, 'attack': 115},
    'silver knight spear': {'weight': 6.0, 'attack': 163},
    'darkmoon bow': {'weight': 1.0, 'attack': 80},
}

def show_weapons(weapons):
    title = 'Weapons'
    print('{}\n{}\n'.format(title, '=' * len(title)))
    for weapon, stats in weapons.items():
        print('{:<40} attack: {:>5} weight: {:5.2f}'.format(weapon.ljust(40, '.'),
                                                            stats.get('attack', 0),
                                                            stats.get('weight', 0.0)))

show_weapons(weapons)
