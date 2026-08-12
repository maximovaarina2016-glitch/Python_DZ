from environs import Env

env = Env()

env.read_env()

DATABASE_URL: str = env.str("DATABASE_URL")

if not DATABASE_URL.endswith("/"):
    raise ValueError("DATABASE_URL must end with a slash '/'")
