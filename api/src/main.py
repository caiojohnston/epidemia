from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.db import qdrant
from src.routers import health


@asynccontextmanager
async def lifespan(app: FastAPI):
    await qdrant.init_collections()
    yield
    await qdrant.close()


app = FastAPI(
    title="Epidemia API",
    version="0.1.0",
    description="API do Epidemia",
    lifespan=lifespan,
)

app.include_router(health.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=settings.port)
