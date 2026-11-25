import os
from flask import Flask, jsonify, render_template, session
from config import Config
from models import db
from routes.auth_routes import auth_bp
from routes.prompt_routes import prompt_bp
from routes.evaluation_routes import evaluation_bp
from routes.history_routes import history_bp


def create_app(config_class=Config):
    """Application factory for Prompt Wise AI."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize SQLAlchemy database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(prompt_bp)
    app.register_blueprint(evaluation_bp)
    app.register_blueprint(history_bp)

    # Global template context processor
    @app.context_processor
    def inject_global_context():
        return {
            "gemini_api_configured": bool(
                app.config.get("GEMINI_API_KEY")
                and app.config.get("GEMINI_API_KEY") != "your_gemini_api_key_here"
            ),
            "gemini_model": app.config.get("GEMINI_MODEL", "gemini-1.5-flash"),
            "current_user": {
                "id": session.get("user_id"),
                "name": session.get("user_name"),
                "email": session.get("user_email"),
            } if "user_id" in session else None,
        }

    # Health check route
    @app.route("/api/health", methods=["GET"])
    def health_check():
        db_status = "connected"
        try:
            db.session.execute(db.text("SELECT 1"))
        except Exception as e:
            db_status = f"error: {str(e)}"

        has_gemini_key = bool(
            app.config.get("GEMINI_API_KEY")
            and app.config.get("GEMINI_API_KEY") != "your_gemini_api_key_here"
        )

        return (
            jsonify(
                {
                    "status": "healthy",
                    "app": "Prompt Wise AI",
                    "version": "1.0.0",
                    "database": db_status,
                    "gemini_api_configured": has_gemini_key,
                }
            ),
            200,
        )

    # Landing Page
    @app.route("/", methods=["GET"])
    def index():
        return render_template("index.html")

    # Error Handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template("base.html", error_title="404 - Page Not Found", error_message="The requested resource could not be found."), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template("base.html", error_title="500 - Internal Server Error", error_message="An unexpected server error occurred."), 500

    # Ensure tables exist
    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
