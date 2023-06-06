import uvicorn

# import http.server
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.config.settings import settings
from app.routes.endpoints import router

app = FastAPI(debug=True)
app.include_router(router)


def custom_openapi():
    openapi_schema = get_openapi(
        title="API python layered architecture",
        version="1.0.0",
        description="This is a Microservice API for Habi",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.APP_HOST,
        port=int(settings.APP_PORT),
    )
