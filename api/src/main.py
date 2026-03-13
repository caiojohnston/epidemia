from fastapi import FastAPI

from src.config import settings
from src.routers import health

app = FastAPI(
    title="Epidemia API",
    version="0.1.0",
    description="API do Epidemia",
)

app.include_router(health.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=settings.port)
