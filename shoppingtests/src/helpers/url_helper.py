import os


def base_url():
    env = os.environ.get("ENV", "test")
    if env.lower() == "test":
        return 'http://localhost:8888/shopping'