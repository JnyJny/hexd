"""hexd Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Settings for hexd."""

    model_config = SettingsConfigDict(
        env_prefix="HEXD",
        env_file=".env-hexd",
    )
    debug: bool = False
