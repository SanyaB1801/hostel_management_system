import tkinter as tk
from tkinter import messagebox
from hostel_management_system import HostelManagementSystem

class HostelManagementGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hostel Management System")
        self.hms = HostelManagementSystem()

        self.room_number_var = tk.StringVar()
        self.capacity_var = tk.IntVar()
        self.new_capacity_var = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        tk.Label(frame, text="Room Number:").grid(row=0, column=0)
        tk.Label(frame, text="Capacity:").grid(row=1, column=0)
        tk.Label(frame, text="New Capacity:").grid(row=2, column=0)

        tk.Entry(frame, textvariable=self.room_number_var).grid(row=0, column=1)
        tk.Entry(frame, textvariable=self.capacity_var).grid(row=1, column=1)
        tk.Entry(frame, textvariable=self.new_capacity_var).grid(row=2, column=1)

        tk.Button(frame, text="Add Room", command=self.add_room).grid(row=3, column=0)
        tk.Button(frame, text="View Rooms", command=self.view_rooms).grid(row=3, column=1)
        tk.Button(frame, text="Update Room", command=self.update_room).grid(row=4, column=0)
        tk.Button(frame, text="Delete Room", command=self.delete_room).grid(row=4, column=1)
        tk.Button(frame, text="Occupy Room", command=self.occupy_room).grid(row=5, column=0)
        tk.Button(frame, text="Unoccupy Room", command=self.unoccupy_room).grid(row=5, column=1)

    def add_room(self):
        room_number = self.room_number_var.get()
        capacity = self.capacity_var.get()
        message = self.hms.add_room(room_number, capacity)
        messagebox.showinfo("Hostel Management System", message)

    def view_rooms(self):
        rooms = self.hms.view_rooms()
        room_list = ""
        for room in rooms:
            room_info = f"Room Number: {room['room_number']}\nCapacity: {room['capacity']}\nOccupied: {room['occupied']}\n\n"
            room_list += room_info
        messagebox.showinfo("Hostel Management System", "Rooms:\n" + room_list)

    def update_room(self):
        room_number = self.room_number_var.get()
        new_capacity = self.new_capacity_var.get()
        messagebox.showinfo("Hostel Management System", self.hms.update_room(room_number, new_capacity))

    def delete_room(self):
        room_number = self.room_number_var.get()
        messagebox.showinfo("Hostel Management System", self.hms.delete_room(room_number))

    def occupy_room(self):
        room_number = self.room_number_var.get()
        messagebox.showinfo("Hostel Management System", self.hms.occupy_room(room_number))

    def unoccupy_room(self):
        room_number = self.room_number_var.get()
        messagebox.showinfo("Hostel Management System", self.hms.unoccupy_room(room_number))

if __name__ == "__main__":
    root = tk.Tk()
    HostelManagementGUI(root)
    root.mainloop()
