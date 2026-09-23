from flask import Flask

# Initialize the Flask application
application = Flask(__name__)

# Define the route for the homepage
@application.route("/")  # <--- Changed from @app to @application
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)