from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced_spell(target: str, power: int) -> list[str]:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequenced_spell


def main() -> None:
    name = "Dragon"
    base_power = 10
    print("\nTesting spell combiner...")
    combined_result = spell_combiner(fireball, heal)(name, base_power)
    result1_part = combined_result[0].split(" for ")[0]
    result2_part = combined_result[1].split(" for ")[0].replace(
        "Heal restores", "Heals")
    print(f"Combined spell result: {result1_part}, {result2_part}")
    print("\nTesting power amplifier...")
    print(f"Original: {base_power}, Amplified: {base_power * 3}")
    # print(power_amplifier(heal, 3)(name, base_power))
    # print("\nTesting conditional caster...")

    # def strong_spell_condition(target: str, power: int) -> bool:
    #     print(target, power)
    #     return power > 15
    # print(conditional_caster(strong_spell_condition, heal)(
    #     name, base_power))
    # print(conditional_caster(strong_spell_condition, heal)(
    #     name, base_power * 2))
    # print("\nTesting spell sequence...")
    # print(spell_sequence([fireball, heal])(name, base_power))


if __name__ == "__main__":
    main()
