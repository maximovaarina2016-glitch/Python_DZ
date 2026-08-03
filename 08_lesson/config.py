from environs import Env

env = Env()

env.read_env()

API_KEY: str = env.str("API_KEY")
BASE_URL: str = env.str("BASE_URL")
TIMEOUT: int = env.int("TIMEOUT", default=60)
DEBUG: bool = env.bool("DEBUG", default=False)

if not BASE_URL.endswith("/"):
    raise ValueError("BASE_URL must end with a slash '/'")
