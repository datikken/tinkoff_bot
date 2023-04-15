from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    token: str
    account_id: Optional[str] = None
    bot_token: Optional[str] = None
    bot_channel: Optional[str] = None
    db_user: Optional[str] = None
    db_pass: Optional[str] = None
    db_name: Optional[str] = None
    sandbox: bool = True

    class Config:
        env_file = ".env"


settings = Settings()
