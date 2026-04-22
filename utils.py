import math


def safe_log(p: float) -> float:
    return math.log(p, 2) if p > 0 else 0.0


def calculate_entropy(probabilities: list) -> float:
    return -sum(p * safe_log(p) for p in probabilities if p > 0)