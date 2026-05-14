from qdrant_client import AsyncQdrantClient
from qdrant_client.models import Distance, VectorParams

from src.config import settings

_COLLECTIONS: dict[str, VectorParams] = {
    "boletins": VectorParams(size=768, distance=Distance.COSINE),
}

_client: AsyncQdrantClient | None = None


def get_client() -> AsyncQdrantClient:
    global _client
    if _client is None:
        _client = AsyncQdrantClient(host=settings.qdrant_host, port=settings.qdrant_port)
    return _client


async def init_collections() -> None:
    client = get_client()
    existing = {c.name for c in (await client.get_collections()).collections}
    for name, params in _COLLECTIONS.items():
        if name not in existing:
            await client.create_collection(collection_name=name, vectors_config=params)


async def close() -> None:
    global _client
    if _client is not None:
        await _client.close()
        _client = None
