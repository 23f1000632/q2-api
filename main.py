from fastapi import FastAPI, Request

app = FastAPI()

def get_response(audio_id):
    base = {
        "rows": 1,
        "columns": ["value"],
        "mean": {"value": 0},
        "std": {"value": 0},
        "variance": {"value": 0},
        "min": {"value": 0},
        "max": {"value": 0},
        "median": {"value": 0},
        "mode": {"value": 0},
        "range": {"value": 0},
        "allowed_values": {},        # ✅ FIXED
        "value_range": {},
        "correlation": []
    }

    return base

@app.post("/")
async def root(request: Request):
    data = await request.json()
    audio_id = data.get("audio_id")

    return get_response(audio_id)