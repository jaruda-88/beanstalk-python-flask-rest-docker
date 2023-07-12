from config import dataclass
from os import path, environ

@dataclass()
class Config:
    BASEDIR : str = path.dirname(path.dirname(path.abspath(__file__)))


def get_config() -> Config:

    env = environ.get("ENV", "DEV")
    match env:
        case "DEV":
            from config.development import Dev
            return Dev()
        case "PRD":
            from config.production import Prd
            return Prd()