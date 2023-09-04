import os


def base_url():
    env = os.environ.get("ENV", "test")
    if env.lower() == "test":
        return 'http://192.168.1.250:8888/shopping'