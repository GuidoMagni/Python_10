from collections.abc import Callable
from typing import Any  # can i? maybe just use an int?


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def more_power(to_add: int) -> int:
        nonlocal initial_power
        initial_power += to_add
        return initial_power
    return more_power


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")
    print("\nTesting spell accumulator...")
    my_power = spell_accumulator(100)
    print(f"Base 100, add 20: {my_power(20)}")
    print(f"Base 100, add 30: {my_power(30)}")
    print("\nTesting enchantment factory...")
    print(enchantment_factory("Flaming")("Sword"))
    print(enchantment_factory("Frozen")("Shield"))
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('secret', 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")


if __name__ == "__main__":
    main()
