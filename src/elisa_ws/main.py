import logging
from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from elisa_ws.conf import settings
from elisa_ws.routers import default
from elisa_ws.routers.v1 import plot
from elisa_ws import __version__

logger = logging.getLogger(__file__)


def create_app():
    _app = FastAPI(
        title='ELISa REST API',
        openapi_prefix=settings.base_url,
        docs_url='/docs/?',
        version=__version__
    )

    # Add CORS middleware
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Create API Router
    api_router = APIRouter()
    api_router.include_router(plot.router, tags=['plot'], prefix='/v1/plot')

    # Add routers to the app
    _app.include_router(default.router, tags=['default'])
    _app.include_router(api_router, prefix='/api')

    return _app


app = create_app()
