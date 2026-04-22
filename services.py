from schemas import ControlEntropyRequest
from utils import calculate_entropy
from fastapi import HTTPException
import math


def compute_control_entropy(data: ControlEntropyRequest):
    dot = data.dot_balls
    single = data.singles
    boundary = data.boundaries

    total = dot + single + boundary

    if total == 0:
        raise HTTPException(status_code=400, detail="Total balls cannot be zero")

    # Outcome probabilities
    p_dot = dot / total
    p_single = single / total
    p_boundary = boundary / total

    distribution = {
        "dot_ball": round(p_dot, 3),
        "single_low": round(p_single, 3),
        "boundary_high": round(p_boundary, 3),
    }

    probs = [p_dot, p_single, p_boundary]

    # Entropy calculation
    entropy = calculate_entropy(probs)

    # Maximum entropy for 3 categories
    max_entropy = math.log(3, 2)

    normalized_entropy = entropy / max_entropy

    # Control score (inverse of entropy)
    control_score = (1 - normalized_entropy) * 100

    # Dominant outcome (NEW INSIGHT)
    dominant_outcome = max(distribution, key=distribution.get)

    # Interpretation logic
    if control_score >= 70:
        tag = "High Control"
        read = "Bowler is highly disciplined with predictable outcomes, indicating strong control over the spell."
    elif control_score >= 40:
        tag = "Moderate Control"
        read = "Bowler shows mixed control with some variability in outcomes."
    else:
        tag = "Low Control"
        read = "Bowling outcomes are highly unpredictable, indicating lack of control and increased volatility."

    return {
        "total_balls": total,
        "distribution": distribution,
        "entropy": round(entropy, 3),
        "normalized_entropy": round(normalized_entropy, 3),
        "control_score": round(control_score, 2),
        "dominant_outcome": dominant_outcome,
        "volatility_tag": tag,
        "tactical_read": read,
    }