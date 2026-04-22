from fastapi import FastAPI
from schemas import ControlEntropyRequest, ControlEntropyResponse
from services import compute_control_entropy

app = FastAPI(title="Control Entropy Model API")


@app.get("/")
def home():
    return {"message": "Control Entropy API is running"}


@app.post("/bowling/control-entropy", response_model=ControlEntropyResponse)
def control_entropy(payload: ControlEntropyRequest):
    return compute_control_entropy(payload)