# 🧾 API Name

Control Entropy Model API

# 🎯 Objective (3–5 lines)

The objective of this API is to quantify how controlled or unpredictable a bowler’s performance is by analyzing the distribution of ball-by-ball outcomes. Instead of relying only on aggregate metrics like economy rate, this model captures the uncertainty in outcomes. It helps distinguish between bowlers who produce consistent, disciplined results and those whose outcomes fluctuate significantly. The API ultimately converts probabilistic uncertainty into a human-interpretable control score.

# 🧠 Scientific Principle Used

This API is based on Shannon Entropy, a concept from information theory.

Entropy measures the uncertainty or randomness in a probability distribution.

A higher entropy value indicates that outcomes are widely spread → more unpredictability → lower control.

A lower entropy value indicates that outcomes are concentrated → more predictability → higher control.

To ensure comparability across different samples, entropy is normalized using the maximum possible entropy for the given number of outcome categories.

# 📥 Input Fields and Data Types

# Field Name			Data Type			Description

dot_balls			integer			Number of deliveries resulting in no runs

singles				integer			Number of deliveries resulting in low scoring (1–2 runs)

boundaries			integer			Number of high-cost deliveries (4s, 6s)

# 🔄 Derived Variables and Their Meaning

1. Outcome Distribution (p)

Each outcome is converted into a probability:

-> p(dot) = dot_balls / total_balls

-> p(single) = singles / total_balls

-> p(boundary) = boundaries / total_balls


👉 This forms the probability distribution, which is essential for entropy calculation.


2. Entropy (q)

Entropy is computed using:

H=−∑p(x)log₂p(x)

👉 Measures how spread out the outcomes are.

3. Normalized Entropy (r)
   
H(norm) =H/(log₂(n)H)
	​
Where n = number of outcome categories (3)

👉 Scales entropy between 0 and 1 for consistency.

4. Control Score (s)

Control=(1−H(norm))×100

👉 Converts uncertainty into a human-friendly metric:

High entropy → low control

Low entropy → high control

5. Dominant Outcome

The outcome category with the highest probability.

👉 Helps identify the bowler’s primary pattern (e.g., dot-heavy vs boundary-prone).

# 📊 Final Output Fields and Their Meaning

-> Field Name	Description

* total_balls	Total deliveries considered
* distribution	Probability distribution of outcomes
* entropy	Raw uncertainty value
* normalized_entropy	Scaled uncertainty (0–1)
* control_score	Final control metric (0–100)
* dominant_outcome	Most frequent outcome type
* volatility_tag	Qualitative classification (High / Moderate / Low Control)
* tactical_read	Human-readable interpretation

# 📤 Example Request

{

  "dot_balls": 12,
  
  "singles": 6,
  
  "boundaries": 6
  
}

# 📥 Example Response

{
  "total_balls": 24,
  
  "distribution": {
  
    "dot_ball": 0.5,
	
    "single_low": 0.25,
	
    "boundary_high": 0.25
	
  },
  
  "entropy": 1.5,
  
  "normalized_entropy": 0.946,
  
  "control_score": 5.4,
  
  "dominant_outcome": "dot_ball",
  
  "volatility_tag": "Low Control",
  
  "tactical_read": "Bowling outcomes are highly unpredictable, indicating lack of control and increased volatility."
  
}


# ⚠️ Validation Errors
-> Condition Error

-> Negative inputs	Rejected by schema validation

-> Total balls = 0	HTTP 400 error: "Total balls cannot be zero"


# ⚙️ Assumptions Made

-> Only three outcome categories are considered (simplified Phase 1 model)

-> All deliveries are treated equally (no weighting for match context)

-> Data provided is already aggregated (not ball-by-ball events)

-> Extras and wickets are not included in this version


# 🧩 Any New Model Fields or Proposed Extensions

For future phases, the model can be extended with:

-> Ball-by-ball event input instead of aggregated counts

-> Additional categories:

-> Wickets

-> Extras

-> Dot variations (e.g., pressure dots)

-> Context-aware weighting:

-> Powerplay vs death overs

-> Match situation (defensive vs attacking bowling)


#💡 Analytical Insight

Traditional metrics like economy rate fail to capture how runs are conceded.

Example:

Bowler A: 1 run every ball → predictable → high control

Bowler B: mix of dots and boundaries → unpredictable → low control

Both may concede similar runs, but entropy reveals the difference in control.

👉 This demonstrates why entropy is a superior analytical metric for this use case.

# 🧱 Project Structure
control-entropy-api/
│

├── main.py          # FastAPI routes

├── schemas.py       # Request/response models

├── services.py      # Core entropy logic

├── utils.py         # Helper functions

├── requirements.txt # Dependencies

├── render.yaml      # Deployment config

└── README.md        # Run instructions


# 🚀 Deployment & Integration Notes

* API follows REST standards
* Accepts JSON payloads
* Can be integrated with frontend dashboards
* Easily extendable to streaming data (Phase 2)
* Compatible with platforms like Render, Railway, or Docker
