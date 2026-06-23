import functools
import operator
from collections.abc import Callable
from typing import Any  # can i?


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    operations: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b,
    }
    try:
        op = operations[operation]
    except KeyError as exc:
        raise ValueError(f"Unknown operation: {operation!r}") from exc
    return functools.reduce(op, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """Create three specialized enchantment casters using functools.partial.

    Each casts with power pre-filled to 50 and a fixed element, leaving
    only `target` to be supplied by the caller.
    """
    fire_caster = functools.partial(
        base_enchantment, power=50, element="fire")
    water_caster = functools.partial(
        base_enchantment, power=50, element="water")
    earth_caster = functools.partial(
        base_enchantment, power=50, element="earth")
    return {
        "fire": fire_caster,
        "water": water_caster,
        "earth": earth_caster,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, memoized via functools.lru_cache."""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0, 1):
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Build and return a functools.singledispatch based spell caster."""
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register
    def _(spell: str) -> str:
        return f"{spell}"

    @cast.register
    def _(spell: list) -> str:
        return f"{len(spell)} spells"
    return cast


def _base_enchantment(power: int, element: str, target: str) -> str:
    return f"Cast {element} enchantment ({power} power) on {target}"


def main() -> None:
    print("\nTesting spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")
    # print("\nTesting partial enchanter...")
    # casters = partial_enchanter(_base_enchantment)
    # for element, caster in casters.items():
    #     print(caster(target="goblin"))
    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    # print(memoized_fibonacci.cache_info())
    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(f"Damage spell: {cast(42)}")
    print(f"Enchantment: {cast('fireball')}")
    print(f"Multi-cast: {cast([1, 2, 3])}")
    print(cast(3.14))


if __name__ == "__main__":
    main()
