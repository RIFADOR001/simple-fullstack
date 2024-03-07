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

if __name__ == "__main__":
    # If the db doesn't exist yet, it is created
    with app.app_context():
        db.create_all()


    app.run(debug=True)


