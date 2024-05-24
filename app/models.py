from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Light(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room = db.Column(db.String(50), nullable=False)
    status = db.Column(db.Boolean, default=False)
    intensity = db.Column(db.Float, default=0.0)
