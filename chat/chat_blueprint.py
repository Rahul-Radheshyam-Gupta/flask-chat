from flask import Blueprint, request, render_template, session, redirect, url_for, jsonify
import random
from string import ascii_uppercase

rooms = {}
chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

def generate_unique_code(length):
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)
        
        if code not in rooms:
            break
    
    return code

@chat_bp.route("/create_or_join", methods=["POST"])
def create_or_join_room():
    session.clear()
    name = request.form.get("name")
    code = request.form.get("code")
    room = request.form.get("room")
    action = request.form.get("action")

    if action == "create":
        room = generate_unique_code(4)
        rooms[room] = {"members": 0, "messages": []}
    elif action == "join":
        room = code
        if code not in rooms:
            return jsonify(request.form), 400
            return render_template("home.html", error="Room does not exist.", code=code, name=name)
    
    session["room"] = room
    session["name"] = name
    return "success", 200

@chat_bp.route("/room")
def room():
    room = session.get('room', None)
    if room is None or session.get("name") is None or room not in rooms:
        return redirect(url_for("index"))
    return render_template('chat/chat.html', name=session['name'], code=session['room'], nums=[1,2])