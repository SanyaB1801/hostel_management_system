from pymongo import MongoClient

class HostelManagementSystem:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://sanyabehera:fmM4k9YG598uQtgn@cluster0.zasc1tj.mongodb.net/')
        self.db = self.client['hostel_management_system']
        self.rooms = self.db['rooms']

    def add_room(self, room_number, capacity):
        if self.rooms.find_one({"room_number": room_number}):
            return f"Room {room_number} already exists."
        room = {"room_number": room_number, "capacity": capacity, "occupied": False}
        self.rooms.insert_one(room)
        return f"Room {room_number} has been added."

    def view_rooms(self):
        rooms = self.rooms.find()
        return [room for room in rooms]

    def update_room(self, room_number, new_capacity):
        self.rooms.update_one({"room_number": room_number}, {"$set": {"capacity": new_capacity}})
        return f"Room {room_number} has been updated."

    def delete_room(self, room_number):
        self.rooms.delete_one({"room_number": room_number})
        return f"Room {room_number} has been deleted."

    def occupy_room(self, room_number):
        self.rooms.update_one({"room_number": room_number}, {"$set": {"occupied": True}})
        return f"Room {room_number} has been occupied."

    def unoccupy_room(self, room_number):
        self.rooms.update_one({"room_number": room_number}, {"$set": {"occupied": False}})
        return f"Room {room_number} has been unoccupied."
