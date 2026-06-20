artifacts = [{'name': 'Fire Staff', 'power': 92, 'type': 'armor'},
             {'name': 'Ice Wand', 'power': 76, 'type': 'relic'},
             {'name': 'Earth Shield', 'power': 69, 'type': 'relic'},
             {'name': 'Crystal Orb', 'power': 85, 'type': 'weapon'}]

mages = [{'name': 'Alex', 'power': 56, 'element': 'light'},
         {'name': 'Morgan', 'power': 77, 'element': 'wind'},
         {'name': 'Kai', 'power': 64, 'element': 'wind'},
         {'name': 'Casey', 'power': 75, 'element': 'light'},
         {'name': 'Casey', 'power': 61, 'element': 'water'}]

spells = ['fireball', 'heal', 'shield']


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    power_levels = list(map(lambda mage: mage['power'], mages))
    avg_power = round(sum(power_levels) / len(power_levels), 2)
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


def main():
    print("\nTesting artifact sorter...")
    sorted = artifact_sorter(artifacts)
    print(f"{sorted[0]['name']} ({sorted[0]['power']} power) comes"
          f" before {sorted[1]['name']} ({sorted[1]['power']} power)")
    # print("\nTesting power filter...")
    # print(power_filter(mages, 62))
    print("\nTesting spell transformer...")
    for spell in spell_transformer(spells):
        print(spell, end=" ")
    # print("\nTesting mage stats...")
    # print(mage_stats(mages))


if __name__ == "__main__":
    main()
