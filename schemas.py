from pydantic import BaseModel, Field


class ControlEntropyRequest(BaseModel):
    dot_balls: int = Field(..., ge=0)
    singles: int = Field(..., ge=0)
    boundaries: int = Field(..., ge=0)


class ControlEntropyResponse(BaseModel):
    total_balls: int
    distribution: dict
    entropy: float
    normalized_entropy: float
    control_score: float
    dominant_outcome: str
    volatility_tag: str
    tactical_read: str