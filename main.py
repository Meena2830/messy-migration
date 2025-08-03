from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="User Management API")

app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "User management API running..."}
