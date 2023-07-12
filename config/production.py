from config.default import Config
from config import dataclass


@dataclass
class Prd(Config):
    DEBUG : bool = False