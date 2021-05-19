from environs import Env

env = Env()
APPLICATION_ENV = env("APPLICATION_ENV", "dev")
env_path = f".env.{APPLICATION_ENV}" if APPLICATION_ENV else None
env.read_env(env_path)

CONFIG: dict = {
    "app": {"env": APPLICATION_ENV},
    "ports": {
        "event_publisher": {
            "type": env("EVENT_PUBLISHER_TYPE", "memory"),
            "topic": env("CHECKED_TOPIC", "status-checked"),
            "server": env("KAFKA_SERVER", "localhost:1234"),
        },
    },
    "repositories": {
        "check_repository": {
            "db_name": env("CHECK_REPO_DB_NAME", "checks"),
            "user": env("CHECK_REPO_DB_USER", "demo"),
            "password": env("CHECK_REPO_DB_PASSWORD", "password"),
            "host": env("CHECK_REPO_DB_PASSWORD", "localhost"),
        }
    }
}
