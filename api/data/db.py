from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
session = db.session
select = db.select