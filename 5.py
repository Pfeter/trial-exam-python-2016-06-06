pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def rich_wooden_legged_pirates(list_of_pirates):
    list_of_rich_wooden_legged_pirates = []
    for pirate in list_of_pirates:
        if pirate['has_wooden_leg'] and int(pirate['gold']) > 15:
            list_of_rich_wooden_legged_pirates.append(pirate['Name'])
    return list_of_rich_wooden_legged_pirates
