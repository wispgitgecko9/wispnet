#####################################################
#WISPNET dbx Patch for dbx1-B  | Created 12.17.2024 #
#####################################################

import tkinter as tk
from tkinter import ttk
import sqlite3

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")

        # Create a container for the layout
        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Create a label for the title
        ttk.Label(self.container, text="Database Records", font=("Arial", 16)).pack(pady=10)

        # Fetch and display the data from the database
        self.display_data()

        # Create blank buttons
        self.create_buttons()

    def create_buttons(self):
        """Create blank buttons."""
        button_frame = ttk.Frame(self.container)
        button_frame.pack(pady=20)

        blank_button1 = ttk.Button(button_frame, text="Blank Button 1")
        blank_button1.pack(side=tk.LEFT, padx=10)

        blank_button2 = ttk.Button(button_frame, text="Blank Button 2")
        blank_button2.pack(side=tk.LEFT, padx=10)

    def display_data(self):
        """Fetch data from the database and display it in a list."""
        # Database connection
        conn = sqlite3.connect("profiles.db")
        cursor = conn.cursor()

        # Fetch data from the profiles table
        cursor.execute("SELECT * FROM profiles")
        rows = cursor.fetchall()

        # Create a Treeview widget to display data
        treeview = ttk.Treeview(self.container, columns=("ID", "First Name", "Middle Name", "Last Name", "Age", "DOB"), show="headings")
        treeview.pack(fill=tk.BOTH, expand=True)

        # Define headings
        treeview.heading("ID", text="ID")
        treeview.heading("First Name", text="First Name")
        treeview.heading("Middle Name", text="Middle Name")
        treeview.heading("Last Name", text="Last Name")
        treeview.heading("Age", text="Age")
        treeview.heading("DOB", text="Date of Birth")

        # Insert data into the Treeview
        for row in rows:
            treeview.insert("", "end", values=row)

        conn.close()

# Main entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
