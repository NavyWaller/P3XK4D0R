from fastapi import FastAPI

app = FastAPI(title="P3XK4D0R API")

@app.get("/")
def root():
    return {"status": "P3XK4D0R online"}

@app.post("/analyze")
def analyze(topic: str):
    return {
        "topic": topic,
        "status": "received",
        "message": "analysis pipeline not implemented yet"
    }