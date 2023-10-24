# from flask import Flask, render_template
# from chat_blueprint import chat_bp
# from flask_socketio import SocketIO


# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config["SECRET_KEY"] = "hjhjsdahhds"
#     app.config.from_mapping(
#         SECRET_KEY='dev'
#     )
#     socketio = SocketIO(app)

#     app.register_blueprint(chat_bp)
#     if test_config is None:
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         app.config.from_mapping(test_config)

    

#     @app.route('/')
#     def index():
#         return render_template('chat/room.html')
    
#     if test_config and test_config.get("send_web_socket"):
#         return app, socketio
#     return app

