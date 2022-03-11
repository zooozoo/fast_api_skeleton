import uvicorn
from fastapi import Depends, FastAPI

from app_one.dependencies import get_query_token, get_token_header
from app_one.internal import admin
from app_one.routers import users, items
from common.im_common import im_common

app_one_api = FastAPI(dependencies=[Depends(get_query_token)])

app_one_api.include_router(users.router)
app_one_api.include_router(items.router)
app_one_api.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)

im_common()


@app_one_api.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


# if __name__ == '__mian__':
uvicorn.run(app_one_api, host='0.0.0.0', port=8000)

