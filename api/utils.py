import os


def require_env_var(env_var_name: str) -> str:
    env_var_value: str | None = os.getenv(env_var_name)
    if env_var_value is None:
        raise ValueError(
            f"{env_var_name} environment variable is required,add it to the .env file in the root of the project"
        )
    return env_var_value
