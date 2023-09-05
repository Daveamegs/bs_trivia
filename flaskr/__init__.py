import os
from flask import Flask, jsonify
from model import setup_db, Question, Category, Difficulty


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)

    # Index Route
    @app.route("/")
    def get_questions():
        return jsonify({
            "success": True,
            "data": "Data is here"
        })

    # Get the List of Available Categories
    @app.route("/categories")
    def get_categories():
        data = Category.query.all()

        if len(data) == 0:
            abort(404)

        return jsonify({
            "Success": True,
            "Data": [cat.name for cat in data]
        })

    # Get All Available Dificulty Levels
    @app.route("/difficulties")
    def get_difficulty():
        data = Difficulty.query.all()

        if len(data) == 0:
            abort(404)

        return jsonify({
            "Success": True,
            "Data": [dif.name for dif in data]
        })

    return app
