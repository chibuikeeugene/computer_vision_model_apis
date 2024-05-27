# BEGIN
import os, sys

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory by going one level up
parent_dir = os.path.dirname(current_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# END     

import typing as t
from fastapi import FastAPI, Request, APIRouter
import uvicorn
from fastapi.responses import HTMLResponse

from api.config import settings
from api.controller import api_router
from api import __version__ as _version
from loguru import logger

app =  FastAPI(
    title = settings.PROJECT_NAME,
    description = "Computer vision api built on convolution neural network moodels for different applications",
    version = _version,
    openapi_url= f"{settings.API_V1_STR}/openapi.json"
)
root_router = APIRouter()

@root_router.get("/")
async def root(request: Request) -> t.Any:
    """Basic HTML response."""
    body = (
            "<html>"
            "<body style='padding: 10px;'>"
            "<h1>Welcome to the API</h1>"
            "<div>"
            "Check the docs: <a href='/docs'>here</a>"
            "</div>"
            "</body>"
            "</html>"
        )

    return HTMLResponse(content=body)


app.include_router(api_router, prefix=settings.API_V1_STR)
app.include_router(root_router)

if __name__ == "__main__":
    # logger.warning("Running in development mode. Do not run like this in production.")

    uvicorn.run(app, host="localhost", port=8001, log_level="debug")
        