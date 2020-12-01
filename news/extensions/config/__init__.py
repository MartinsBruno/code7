#Mongo configuration
url = "localhost"
port = "27017"

def init_app(app):
    app.config["SECRET_KEY"] = "\x822\x04\x1d\t\xdb\x8c\x07f\xc3\x18W\xedz\x1e\xac"
    app.config["MONGO_URI"] = f"mongodb://{url}:{port}/sevencode"