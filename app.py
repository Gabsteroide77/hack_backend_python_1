from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/users", methods = ["GET"])
def fn_users_get():
    return jsonify({
        "payload" : "success"
    })

@app.route("/user", methods = ["POST"])
def fn_user_post():
    return jsonify({
        "payload" : "success"
    })

@app.route("/user", methods = ["DELETE"])
def fn_delete():
    return jsonify({
        "payload" : "success" 
    })

@app.route("/user", methods = ["PUT"])
def fn_user_put():
    return jsonify({
    "payload": "success",
    "error": False
    })

@app.route("/api/v1/users", methods = ["GET"])
def fn_get_users_api():
    return jsonify({
        "payload" : []
    })

@app.route("/api/v1/user", methods = ["POST"])
def fn_post_users_api():
    return jsonify({
        "payload": {
            "email": request.args.get("email"),
            "name": request.args.get("name")
        }
#http://localhost:5000/api/v1/user?email=foo@foo.foo&name=fooziman
    })

@app.route("/api/v1/user/add", methods = ["POST"])
def fn_post_user_add_api():
    return jsonify({
        "payload":{
        "email": request.form.get("email"),
        "name": request.form.get("name"),
        "id": request.form.get("id")
        }
    })

@app.route("/api/v1/user/create", methods = ["POST"])
def fn_users_create_api():
    data = request.get_json()
    return  jsonify({
        "payload": {
            "email": data["email"],
            "name": data["name"],
            "id": data["id"]
        }
    })

if __name__ == "__main__":
    app.run(debug=True)