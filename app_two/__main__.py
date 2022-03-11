import uvicorn
from fastapi import Depends, FastAPI

from app_two.dependencies import get_query_token, get_token_header
from app_two.internal import admin
from app_two.routers import users, items
from common.im_common import im_common

sleleton_app = FastAPI(dependencies=[Depends(get_query_token)])

sleleton_app.include_router(users.router)
sleleton_app.include_router(items.router)
sleleton_app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

im_common()


@sleleton_app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# if __name__ == '__mian__':
uvicorn.run(sleleton_app, host='0.0.0.0', port=8000)

