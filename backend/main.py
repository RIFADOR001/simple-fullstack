from flask import request, jsonify
from config import app, db
from models import Contact

# CRUD Create Read Update Delete

# create
# - first_name
# - last_name
# - email

# Here we specify the valid methods
@app.route("/contacts", methods=["GET"])
def get_contacts():
    # We get all the contacts
    contacts = Contact.query.all()
    # We convert the Python objects into a map with json elements
    # Then we convert the map into a list
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400
        )

    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    # return jsonify({"first_name":first_name, "last_name": last_name, "email":email})
    return jsonify({"message": "User created!"}), 201


if __name__ == "__main__":
    # If the db doesn't exist yet, it is created
    with app.app_context():
        db.create_all()


    app.run(debug=True)


