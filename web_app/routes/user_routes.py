from flask import Blueprint, jsonify, request, render_template #, flash, redirect
from web_app.models import db, parse_records
user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/books.json")
def list_books():
    #books = [
       # {"id": 1, "title": "Book 1"},
       # {"id": 2, "title": "Book 2"},
       # {"id": 3, "title": "Book 3"},
    #]
    user_records = user_records.query.all()
    print(user_records)
    users = parse_records(user_records)
    return jsonify(user)

@user_routes.route("/books")
def list_books_for_humans():
    books = [
        {"id": 1, "title": "Book 1"},
        {"id": 2, "title": "Book 2"},
        {"id": 3, "title": "Book 3"},
    ]
    return render_template("user.html", message="Here's some books", books=books)

@user_routes.route("/books/new")
def new_user():
    return render_template("new_user.html")

@user_routes.route("/user/create", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))
    # todo: store in database

    new_user = User(title=request.form["title"], author_id=request.form["author_name"])
    db.session.add(new_book)
    db.session.commit()
    
    
    return jsonify({
        "message": "USER CREATED OK (TODO)",
        "book": dict(request.form)
    })
    #flash(f"Book '{new_book.title}' created successfully!", "success")
    #return redirect(f"/books")