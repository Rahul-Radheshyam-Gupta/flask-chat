# from flask import session
# from flask_socketio import join_room, leave_room, send
# from chat import create_app
# from chat_blueprint import rooms
# from datetime import datetime

# app, socketio = create_app({'send_web_socket': True})

# @socketio.on("message")
# def message(data):
#     print("emitted message socket.....")
#     room = session.get("room")
#     if room not in rooms:
#         return 
    
#     content = {
#         "name": session.get("name"),
#         "message": data["data"],
#         "created_at": datetime.now().strftime("%d %b %Y at %H:%M")
#     }
#     send(content, to=room)
#     rooms[room]["messages"].append(content)
#     print(f"\n\n{session.get('name')} said: {data['data']}\n")

# @socketio.on("connect")
# def connect(auth):
#     room = session.get("room")
#     name = session.get("name")
#     if not room or not name:
#         return
#     if room not in rooms:
#         leave_room(room)
#         return
    
#     join_room(room)
#     send({"name": name, "message": "has entered the room"}, to=room)
#     rooms[room]["members"] += 1
#     print(f"{name} joined room {room}")

# @socketio.on("disconnect")
# def disconnect():
#     print("\n Disconnected \n\n ...........")
#     room = session.get("room")
#     name = session.get("name")
#     leave_room(room)

#     if room in rooms:
#         rooms[room]["members"] -= 1
#         if rooms[room]["members"] <= 0:
#             del rooms[room]
    
#     send({"name": name, "message": "has left the room"}, to=room)
#     print(f"{name} has left the room {room}")