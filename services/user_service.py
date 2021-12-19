from models.user_model import UserModel, db
from werkzeug.security import generate_password_hash, check_password_hash


class UserService:
    def register_user(self, form):
        name = form.username.data
        email = form.email.data
        password = form.password.data

        user = UserModel.query.filter_by(email=email).first()
        if user:
            return None

        hash_password = generate_password_hash(password,
                                               'pbkdf2:sha256',
                                               salt_length=8)
        new_user = UserModel(name=name,
                             email=email,
                             password=hash_password)

        db.session.add(new_user)
        db.session.commit()
        return new_user

    def get_user_by_id(self, user_id):
        return UserModel.query.get(user_id)

    def login_user(self, form):
        email = form.email.data
        password = form.password.data

        user = UserModel.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                return user

        return None
