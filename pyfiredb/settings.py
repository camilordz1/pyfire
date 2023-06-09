from dataclasses import dataclass
from environs import Env
import json


env = Env()
env.read_env()


@dataclass
class Settings:
    setup = json.loads(env("DB_SETUP"))


@dataclass
class Credentials:
    user = env("DB_USER")
    password = env("DB_PASS")
