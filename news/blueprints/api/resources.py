from flask import Blueprint, jsonify, request, current_app, Response
from news.extensions.database import mongo
from bson.json_util import dumps, loads

bp = Blueprint("api", __name__, url_prefix="/api")

@bp.route("/authors", methods=["GET"])
def getAuthors():
    """Return all authors"""
    collection = mongo.db.authors
    query = collection.find()
    if query.count() >= 1:
        json_string = dumps(query)
        return Response(json_string, mimetype="application/json")
    else:
        return jsonify({"Response": "There are no registered authors"})

@bp.route("/authors", methods=["POST"])
def postAuthors():
    """Create a new Author""" 
    collection = mongo.db.authors
    query = collection.find_one({"Name": request.json["name"]})
    if query:
        return jsonify({"Response": "Author already exist"})
    else:   
        collection.insert({"Name":request.json["name"]})
        return jsonify({"Response": "Author registered"})

@bp.route("/authors/<name>", methods=["PUT"])
def putAuthors(name):
    """Update a existing author"""
    collection = mongo.db.authors
    query = collection.find_one({"Name": name})
    if query:
        if collection.find_one({"Name": request.json["name"]}):
            return jsonify({"Response": "There is already a registered author with that name"})
        else:
            collection.update_one({"Name": name}, {"$set": {"Name":request.json["name"]}})
            return jsonify({"Response": "Author updated"})
    else:
        return jsonify({"Response": "There is no author with that name"})

@bp.route("/authors/<name>", methods=["DELETE"])
def deleteAuthors(name):
    """Delete a existing author"""
    collection = mongo.db.authors
    query = collection.find_one({"Name": name})
    if query:
        collection.delete_one({"Name": name})
        return jsonify({"Response": "Author successfully deleted"})
    else:
        return jsonify({"Response": "There is no author with that name"})

@bp.route("/news", methods=["GET"])
def getNews():
    """Return all news"""
    collection = mongo.db.news
    query = collection.find()
    if query.count() >= 1:
        json_string = dumps(query)
        return Response(json_string, mimetype="application/json")
    else:
        return jsonify({"Response": "There are no registered news"})

@bp.route("/news/<parameter>", methods=["GET"])
def getNewsByTitle(parameter):
    """Return all news"""
    collection = mongo.db.news
    queryByTitle = collection.find_one({"title": parameter})
    queryByText = collection.find_one({"text": parameter})
    queryByAuthor = collection.find({"author": parameter})
    if queryByTitle:
        json_string = dumps(queryByTitle)
        return Response(json_string, mimetype="application/json")
    elif queryByText:
        json_string = dumps(queryByText)
        return Response(json_string, mimetype="application/json")
    elif queryByAuthor:
        json_string = dumps(queryByAuthor)
        return Response(json_string, mimetype="application/json")
    else:
        return jsonify({"Response": "There are no registered news"})

@bp.route("/news", methods=["POST"])
def postNews():
    """Create a new node""" 
    collection = mongo.db.news
    _title = request.json["title"]
    _text = request.json["text"]
    _author = request.json["author"]
    if _title and _text and _author:
        authorCollection = mongo.db.authors
        queryAuthor = authorCollection.find_one({"Name": _author})
        queryTitle = collection.find_one({"title": _title})
        print(queryTitle)
        if queryTitle:
            return jsonify({"Response": "One news item already has this title"})
        if queryAuthor:
            collection.insert({"title": _title, "text": _text, "author": _author})
            return jsonify({"Response": "Successfully registered news"})
        else:
            return jsonify({"Response": "There is no registered author with that name"})
    else:
        return jsonify({"Response": "Missing arguments"})

@bp.route("/news/<title>", methods=["PUT"])
def putNews(title):
    """Update a existing node"""
    collection = mongo.db.news
    _new_title = request.json["title"]
    _text = request.json["text"]
    _author = request.json["author"]
    if _new_title and _text and _author:
        query = collection.find_one({"title": title})
        authorCollection = mongo.db.authors
        if query:
            authorQuery = authorCollection.find_one({"Name": _author})
            if authorQuery:
                collection.update_one({"title": title}, {"$set": {"title": _new_title, "text": _text, "author": _author}})
                return jsonify({"Response": "Successfully updated news"})        
            else:
                return jsonify({"Response": "There are no authors with the desired name"})
        else:
            return jsonify({"Response": "You do not have a news item with the title informed"})
    else:
        return jsonify({"Response": "Missing arguments"})

@bp.route("/news/<title>", methods=["DELETE"])
def deleteNews(title):
    """Delete a existing node"""
    collection = mongo.db.news
    query = collection.find_one({"title": title})
    if query:
        collection.delete_one({"title": title})
        return jsonify({"Response": "Node successfully deleted"})
    else:
        return jsonify({"Response": "There is no node with that name"})