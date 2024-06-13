from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(config_class)

    db.init_app(app)
    login.init_app(app)

    from app.models import User  # 导入 User 模型

    from app.views.auth import auth_bp
    from app.views.main import main_bp
    from app.views.user import user_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(main_bp)
    app.register_blueprint(user_bp, url_prefix='/user')

    @login.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app


