from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.router.app_routers import app_router

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Vet App",
        version="1.0.0",
        description="This is a very custom OpenAPI schema",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.include_router(app_router)
