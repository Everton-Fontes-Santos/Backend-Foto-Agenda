from config.variables import config
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from tortoise.contrib.fastapi import register_tortoise

# from controllers.debitController import debit_router
# from controllers.tokenController import token_router
app = FastAPI()

# app.include_router(debit_router, tags=['Debits'])
# app.include_router(token_router, tags=['Token'])


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


register_tortoise(
    app=app,
    db_url=config.database_url,
    modules={"models": config.tortoise_models},
    generate_schemas=True,
    add_exception_handlers=True,
)
