from flask import Flask
from flasgger import Swagger
from config.swagger import get_swagger_config, get_swagger_template
from config.default import get_config


def create_app() -> Flask:
    '''
    init app
    :return app: flask application
    '''

    from flask_cors import CORS
    
    app = Flask(__name__)

    # [set cross domain]
    CORS(app)

    # [ set config ]
    app.config.from_object(get_config())

    # [ resister api ]
    
    # [ set swagger ]
    Swagger(app, config=get_swagger_config(), template=get_swagger_template())

    return app


application = create_app()


if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5040, debug=application.config["DEBUG"])