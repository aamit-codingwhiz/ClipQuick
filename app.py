# app.py
from flask import Flask
from models.url import db
from routes.shorten_url import shorten_url_bp
from routes.view_all_urls import view_all_urls_bp
from config import Config

app = Flask(
    import_name=__name__
)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register blueprints
app.register_blueprint(
    blueprint=shorten_url_bp
)
app.register_blueprint(
    blueprint=view_all_urls_bp
)

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
