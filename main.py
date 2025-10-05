from website import create_app,db,limiter , render_template
from werkzeug.security import generate_password_hash, check_password_hash
from website.models import User

app = create_app()
with app.app_context():
    db.create_all()
    limiter.init_app(app)
    admin_email = "admin@example.com"
    admin_password = "admin1234"

    existing_admin = User.query.filter_by(email=admin_email).first()

    if existing_admin:
        print("Admin user already exists!")
    else:
        admin_user = User(
            email=admin_email,
            name="Admin",
            password=generate_password_hash(admin_password, method='pbkdf2:sha256'),
            token=None,
            is_admin=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")

if __name__ == '__main__':
    app.run("0.0.0.0",debug=True)
