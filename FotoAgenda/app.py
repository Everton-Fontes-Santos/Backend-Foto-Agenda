import uvicorn
from config.variables import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.client_model import Client_Pydantic, ClientModel
from starlette.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise
from utils.api.post_items import post_items

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_origins=["*"],
)


@app.get("/")
async def redirect_to_doc():
    return RedirectResponse("/docs")


@app.get("/healthcheck")
async def healthcheck():
    return {"message": "ok"}


@post_items(ClientModel, Client_Pydantic)
@app.post("/item")
async def post(items: list[Client_Pydantic]):
    ...


register_tortoise(
    app=app,
    db_url=config.database_url,
    modules={"models": config.tortoise_models},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=config.PORT, log_level="info")
