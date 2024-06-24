# Hostel Management System

A simple hostel management system built with Tkinter for the GUI and MongoDB for the database.

## Features

- **Add Rooms:** Add new rooms with specific room numbers and capacities.
- **View Rooms:** Display a list of all rooms with their details.
- **Update Room Capacity:** Modify the capacity of existing rooms.
- **Delete Rooms:** Remove rooms from the system.
- **Occupy/Unoccupy Rooms:** Mark rooms as occupied or unoccupied.

## Installation

### Prerequisites

- Python 3.x
- MongoDB

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HostelManagementSystem.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd HostelManagementSystem
   ```

3. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python src/gui.py
   ```

## Usage

1. **Add Room:**
   - Enter the room number and capacity.
   - Click the "Add Room" button.

2. **View Rooms:**
   - Click the "View Rooms" button to see a list of all rooms.

3. **Update Room Capacity:**
   - Enter the room number and the new capacity.
   - Click the "Update Room" button.

4. **Delete Room:**
   - Enter the room number.
   - Click the "Delete Room" button.

5. **Occupy Room:**
   - Enter the room number.
   - Click the "Occupy Room" button.

6. **Unoccupy Room:**
   - Enter the room number.
   - Click the "Unoccupy Room" button.

## Dependencies

- `pymongo`: Python driver for MongoDB.
- `tkinter`: Standard Python interface to the Tk GUI toolkit.

You can install these dependencies using the `requirements.txt` file provided.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.
