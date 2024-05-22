import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:siya@localhost/youtube_blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY =  os.getenv("SECRET_KEY")
    JWT_SECRET_KEY =  os.getenv("SECRET_KEY")
