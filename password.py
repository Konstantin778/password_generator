from enum import IntEnum
from math import log2
import secrets


class StrengthToEntropy(IntEnum):
    bad = 0
    weak = 30
    good = 50
    strong = 70
    excellent = 110

def create_new(length: int, characters: str) -> str:
    return ''.join(secrets.choice(characters) for _ in range(length))


def get_entropy(length: int, character_number: int) -> float:
    try:
        entropy = length * log2(character_number)
    except ValueError:
        return 0.0

    return round(entropy, 2)

