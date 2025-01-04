from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    app_name: str = "My FastAPI App"
    admin_email: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
