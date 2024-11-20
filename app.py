import os
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import router

load_dotenv()

app = FastAPI(docs_url="/api/docs", openapi_url="/api/openapi.json")

app.include_router(router)

APP_PORT = int(os.getenv("APP_PORT", 5001))


# Health check endpoint
@app.get("/ping")
async def health_check():
    return {"status": True, "message": "Text Eval Service is working"}


if __name__ == "__main__":
    import uvicorn

    num_workers = os.cpu_count() or 1
    uvicorn.run("app:app", host="0.0.0.0", port=APP_PORT, debug=False, workers=num_workers)
