from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    @property
    def config(self) -> dict:
        return {
            key.upper(): value
            for key, value in self.model_dump().items()
        }
