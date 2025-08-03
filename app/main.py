from fastapi import FastAPI
from app.routes import router  # Make sure routes/__init__.py contains the router

app = FastAPI(title="User Management API")

# Include your application routes
app.include_router(router)

# Health check endpoint
@app.get("/")
def health_check():
    return {"message": "User management API running..."}
