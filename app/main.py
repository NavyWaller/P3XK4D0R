from fastapi import FastAPI
from app.agents.coordinator_agent import coordinator_agent
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="P3XK4D0R API")

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)

@app.get("/")
def root():
    return {"status": "P3XK4D0R online"}

@app.post("/analyze")
async def analyze(topic: str):

    result = await coordinator_agent(topic)

    return result