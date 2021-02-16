from fastapi import FastAPI
from api import video_router

from db import database


app = FastAPI()

app.state.database = database


app.include_router(video_router)


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()


# 42 Minuta 

