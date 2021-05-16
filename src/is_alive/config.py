from environs import Env

env = Env()
APPLICATION_ENV = env("APPLICATION_ENV", None)
env_path = f".env.{APPLICATION_ENV}" if APPLICATION_ENV else None
env.read_env(env_path)

application_env = env("APPLICATION_ENV", "dev")

CONFIG: dict = {
    "app": {"env": application_env},
    "ports": {
        "event_publisher": {
            "type": env("EVENT_PUBLISHER_TYPE", "memory"),
            "topic": env("CHECKED_TOPIC", "status-checked"),
            "server": env("KAFKA_SERVER", "localhost:1234"),
        }
    },
}
