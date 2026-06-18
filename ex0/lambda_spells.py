# === Exercise 0 Test Data ===
# # Lambda Sanctum Test Data
# mages = [{'name': 'Alex', 'power': 56, 'element': 'light'}, {'name': 'Morgan', 'power': 77, 'element': 'wind'}, {'name': 'Kai', 'power': 64, 'element': 'wind'}, {'name': 'Casey', 'power': 75, 'element': 'light'}, {'name': 'Casey', 'power': 61, 'element': 'water'}]
# spells = ['blizzard', 'darkness', 'tornado', 'heal']

import typing
import itertools
import collections.abc
# import sorted
# import map, filter, min, max, round, sum, len

artifacts = [{'name': 'Ice Wand', 'power': 119, 'type': 'accessory'}, {'name': 'Water Chalice', 'power': 105, 'type': 'weapon'}, {'name': 'Light Prism', 'power': 97, 'type': 'armor'}, {'name': 'Shadow Blade', 'power': 91, 'type': 'focus'}]

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return(sorted(artifacts))
