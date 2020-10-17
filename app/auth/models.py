from datetime import datetime
from app import db, bcrypt, login_manager   # app/__init__.py
from flask_login import UserMixin

# creating a users table from User class
class User(UserMixin, db.Model):
    __tablename__ = 'users_book'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.now)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    #class methods belong to a class but not associated with class instance.
    @classmethod
    def create_user(cls, user, email, password): # we have used here cls insread of self. self is used for instance.
        user = cls(user_name=user,
                   user_email=email,
                   user_password=bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()

        return user

@login_manager.user_loader #its instance of login_manager
def load_user(id):
    return User.query.get(int(id))