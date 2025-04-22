from flask import Blueprint ,render_template,request, jsonify
from models import db , User
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<h1>Logout Page</h1>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()  # دریافت داده‌ها به صورت JSON از درخواست
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@auth.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    return jsonify({"message": "User not found!"}), 404