from app import create_app, db  # from the app package __init__
from app.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev') #we are passing config dev here. it will use dev.py config for db connections.
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
    flask_app.run()
