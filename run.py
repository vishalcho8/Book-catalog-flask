from app import create_app, db  # from the app package __init__
from app.auth.models import User
from sqlalchemy import exc

#if __name__ == '__main__':
flask_app = create_app('prod') #we are passing config dev here. it will use dev.py config for db connections.
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(user_name='harry').first():
            User.create_user(user='harry', email='harry@potters.com', password='secret')
    except exc.IntegrityError:
        flask_app.run()
