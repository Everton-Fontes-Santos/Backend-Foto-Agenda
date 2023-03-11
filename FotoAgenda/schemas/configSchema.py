from pydantic import BaseSettings, Field


class Config(BaseSettings):
    database_url: str = Field(..., env="DATABASE_URL")
    tortoise_models: list[str] = Field(..., env="MODELS")
    PORT: int = Field(5000, env="PORT")
