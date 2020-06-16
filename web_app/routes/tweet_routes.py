from flask import Blueprint

tweet_routes = Blueprint("tweet_routes", __name__)

@tweet_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@tweet_routes.route("/about")
def about():
    return "About me"