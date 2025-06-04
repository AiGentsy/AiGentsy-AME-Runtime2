from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent_runtime_container import agent_graph

app = FastAPI()

# Optional: CORS for browser/JS access (safe to leave for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend domain(s) in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/trigger")
async def trigger_agent(request: Request) -> dict:
    try:
        data = await request.json()
        user_input = data.get("input", "Hello from AiGentsy")
        result = agent_graph.invoke({"input": user_input})
        return {"output": result["output"]}
    except Exception as e:
        return {"error": str(e)}

# 🚀 Entrypoint for Railway container to run FastAPI
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
