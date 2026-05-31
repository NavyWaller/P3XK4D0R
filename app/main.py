from fastapi import FastAPI
from app.agents.coordinator_agent import coordinator_agent
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="P3XK4D0R API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/reports",
    StaticFiles(directory="reports"),
    name="reports"
)

@app.get("/")
def root():
    return {"status": "P3XK4D0R online"}

class ReportRequest(BaseModel):

    topic: str

    use_memory: bool = True

    use_geopolitical: bool = True
    use_technical: bool = True
    use_risk: bool = True

@app.post("/analyze")
async def analyze(request: ReportRequest):

    result = await coordinator_agent(request)

    return result