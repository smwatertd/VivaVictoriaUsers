from core.settings.settings import Settings

from pydantic_settings import SettingsConfigDict


class AppSettings(Settings):
    debug: bool = False

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore',
    )
