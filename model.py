# Import dependencies
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
import os
from dotenv import load_dotenv

# Initialize python dotenv
load_dotenv()

# Get environment variables
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_HOST = os.environ.get("DB_HOST")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_TYPE = os.environ.get("DB_TYPE")
DB_PORT = os.environ.get("DB_PORT")

# Database URI
DB_URI = '${DB_TYPE}://${DB_USER}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}'

db = SQLAlchemy()

# Database Setup function
def setup_db(app, db_uri = DB_URI):
    with app.app_context():
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
        db.app = app
        db.init_app(app)
        db.create_all()


# The Question Model
class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key= True)
    question = Column(String)
    possible_answers = Column(String)
    correct_answer = Column(String)
    difficulty = Column(String)
    category = Column(String)
    continent = Column(String)

    def __init__(self, question, possible_answers, correct_answer, difficulty, category, continent):
        self.question = question
        self.possible_answers = possible_answers
        self.correct_answer = correct_answer
        self.difficulty = difficulty
        self.category = category
        self.continent = continent

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return{
            "ID": self.id,
            "Question": self.question,
            "Possible Answers": self.possible_answers,
            "Correct Answer": self.correct_answer,
            "Category": self.category,
            "Difficulty": self.difficulty,
            "Continent": self.continent
        }

class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def format(self):
        return{
            "ID": self.id,
            "Name": self.name
        }

class Difficulty(db.Model):
    __tablename__ = "difficulty"

    id = Column(Integer, primary_key = True)
    name = Column(String)

    def __init__(self, name):
        self.name = name

    def format(self):
        return{
            "ID" : self.id,
            "Name": self.name
        }