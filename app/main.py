from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.vectorStore import build_index
from app.utils.corsConfig import allow_cors

app = FastAPI(title="THRSL Chatbot Service")

# allow cors
allow_cors(app)

@app.on_event("startup")
def startup_event():
    try:
        build_index() # fetch data from mssql and build data
        print("✅ Knowledge index built successfully")
    except Exception as e:
        print("❌ Failed to build index:", e)
        raise

app.include_router(chat_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok", "service": "chatbot"}
