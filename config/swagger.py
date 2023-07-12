from config import dataclass, field, asdict
from typing import Dict, List


@dataclass(frozen=True)
class SwaggerConfig:
    title : str = "SWAGGER API"
    uiversion : int = 3
    headers : List[str] = field(default_factory = lambda : [])
    specs : List[str] = field(default_factory = lambda : [
                                                            { 
                                                                "endpoint": 'swagger_api',
                                                                "route": '/swagger_api_spec.json',
                                                                "rule_filter": lambda rule: True,  # all in
                                                                "model_filter": lambda tag: True,  # all in 
                                                            }
                                                        ]) 
    static_url_path : str = "/help" # http swagger url /help or /docs
    specs_route : str = "/help/"


@dataclass(frozen=True)
class SwaggerTemplate:
    swagger : str = "2.0"
    info : Dict[str, str] = field(default_factory = lambda : (
                                                                {
                                                                    "title": "Swagger API",
                                                                    "description": "Api for test",
                                                                    "version": "1.0.0",        
                                                                    "openapi_version": "3.0.2",
                                                                    "contact": {
                                                                        "name": "project source",
                                                                        "url": ""
                                                                    }   
                                                                }
                                                             )) 


def get_swagger_config() -> dict:
    return asdict(SwaggerConfig())


def get_swagger_template() -> dict:
    return asdict(SwaggerTemplate())