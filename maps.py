# Maps
import random
from tabulate import tabulate


def append_list(dictionary, list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)


def replace_tile(list, tile1, tile2):
    """Make sure that replaced tiles do not overwrite each other"""
    while random_tile(list, tile1) == random_tile(list, tile2):
            random_tile(list, tile1)
            random_tile(list, tile2)


def random_tile(list, tile):
    """Choose a random tile to replace and return the indices"""
    x = random.choice(list)
    y = random.choice(x)
    n = list.index(x)
    m = x.index(y)
    list[n][m] = tile
    return (n, m)


def generate_map(list):
    """randomly generate a 3x3 city map from tile types"""
    map = [[random.choice(list) for i in range(3)] for j in range(3)]
    # add boss and start tiles
    replace_tile(map, "Final Enemy", "Start")
    return map


def print_map(dictionary):
    """print out each city map generated"""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        # format the maps in rows and columns
        print(tabulate(map, tablefmt=" "))
        print("\n")

locations = ['City Tower', 'Shopping Centre', 'Sewer']

map_tiles = {"Guard": {"description": "location of a Guard",
                       "action": "must defeat the enemy to continue"},
             "Final Enemy": {"description":
                             "Location of the final enemy",
                             "action": "fight the final enemy"
                             "may run away or fight the boss to continue"},
             "Supplies": {"description":
                          "location of potential healing items or weapons",
                          "action": "explore"},
             " ": {"description":
                   "location with no items",
                   "action": "may rest or move to another location"},
             "Start": {"description": "entrance to the location",
                       "action": "may rest or move to another location"},
             "Oxygen Station": {"description": "can fill up your oxygen tank",
                                "action": "fill up your oxygen tank"}
             }


# generate a list of cities
city_level = []
append_list(locations, city_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Final Enemy")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for city in city_level:
    city_map = generate_map(tile_types)
    main_map[city] = city_map
