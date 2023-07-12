from config.default import Config
from config import dataclass


@dataclass
class Dev(Config):
    DEBUG : bool = True