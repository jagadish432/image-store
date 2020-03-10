import os
import uuid
from config import PROJECT_ROOT, DATABASE_NAME
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import *


database_file = os.path.join(PROJECT_ROOT, 'db', DATABASE_NAME)
db = SQLAlchemy()


class ImageStore(db.Model):
    __tablename__ = 'ImageStore'
    id = db.Column(VARCHAR(50), nullable=False, primary_key=True)  # unique id (UUID) for each uploaded image
    name = db.Column(VARCHAR(1000), nullable=False)  # image name
    shortenedURL = db.Column(VARCHAR(1000), nullable=False)  # shortened URL
    visitsCount = db.Column(Integer, nullable=False, server_default="0")  # number of times visited to access the image
    passwordOpted = db.Column(Boolean, nullable=False)  # opted for password protection
    password = db.Column(VARCHAR(100), nullable=True)  # hashed password to validate before accessing the image via URL
    content = db.Column(BLOB, nullable=False)  # content of file in BLOB

    def __repr__(self):
        return "<Name: {} and shortenedURL: {}>".format(self.name, self.shortenedURL)

    def __init__(self, filename, content, password_protected, password):
        self.id = str(uuid.uuid4())
        self.name = filename
        self.shortenedURL = self.id
        self.passwordOpted = password_protected
        self.password = password
        self.content = content
