from flask import Blueprint

tweets_users = Blueprint("tweets_users", __name__)

@tweets_users.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@tweets_users.route("/about")
def about():
    return "About me"