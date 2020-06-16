from flask import Flask

from web_app.models import db, migrate
from web_app.routes.tweet_routes import tweet_routes
from web_app.routes.user_routes import user_routes

DATABASE_URI = "sqlite:///web_app_99.db" # using relative filepath
#DATABASE_URI = "sqlite:////Users/Username/Desktop/your-repo-name/web_app_99.db" # using absolute filepath on Mac (recommended)
#DATABASE_URI = "sqlite:///C:\\Users\\Username\\Desktop\\your-repo-name\\web_app_99.db" # using absolute filepath on Windows (recommended) h/t: https://stackoverflow.com/a/19262231/670433

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tweet_routes)
    app.register_blueprint(user_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)