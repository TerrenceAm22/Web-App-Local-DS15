from flask import Flask

from web_app.tweet_routes import tweets_users
#from web_app.routes.book_routes import book_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tweets_users)
    #app.register_blueprint(book_routes)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)