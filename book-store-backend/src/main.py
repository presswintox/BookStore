import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    default_response_class=ORJSONResponse,
    description="API для работы с книгами. "
    "Используется полнотекстовый поиск из ElasticSearch.",
)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
    )
