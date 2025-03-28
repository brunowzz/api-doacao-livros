from flask import Flask

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    from .config import Config
    app.config.from_object(Config)
    
    from .database.db import init_app
    init_app(app)
    
    from .routes.livros_routes import livros_bp
    app.register_blueprint(livros_bp)
    
    return app