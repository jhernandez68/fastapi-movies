from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """_summary_

    Args:
        BaseSettings (_type_): _description_
    """
    app_name: str = "Backend of SimpleMovies"
    db_uri: str="sqlite:///./sql_app.db"
    bcrypt_algorithm: str="HS256"
    jwt_secret: str="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    access_token_expire_minutes: int=30
    
    model_config = SettingsConfigDict(env_file=".env")