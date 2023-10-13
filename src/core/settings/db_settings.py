from core.settings.settings import Settings

from pydantic import Field

from pydantic_settings import SettingsConfigDict


class DBSettings(Settings):
    driver: str = 'postgresql'
    host: str = 'localhost'
    port: int = 5432
    user: str = 'postgres'
    password: str = 'postgres'
    db: str = 'postgres'
    echo: bool = Field(default=False, alias='echo')

    model_config = SettingsConfigDict(
        env_file='.env',
        env_prefix='POSTGRES_',
        extra='ignore',
    )

    @property
    def url(self) -> str:
        return f'{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'

    @property
    def config(self) -> dict:
        return {
            'SQLALCHEMY_DATABASE_URI': self.url,
        }
