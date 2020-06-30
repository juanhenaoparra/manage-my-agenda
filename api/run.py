from flask import Flask, request, Response, jsonify
from database.db import initialize_app


app = Flask(__name__)
initialize_app(app)

if __name__ == "__main__":
  app.run(debug=True)
