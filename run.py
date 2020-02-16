from app import app
from db import db

db.init(app)

@app.before_first
def create_tables():
    db.create_all()
