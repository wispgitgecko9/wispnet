#####################################################
#WISPNET dbx Patch Unused-X1   | Created 12.17.2024 #
#####################################################

import sqlite3
import tkinter as tk
from tkinter import ttk

class DatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer and Profile Creator")

        # Set a fixed size for the window
        self.root.geometry("800x600")  # Width x Height
        self.root.maxsize(1200, 800)   # Max size the window can expand to
        self.root.minsize(800, 600)    # Min size to prevent resizing to a smaller window

        # Create a container for the layout
        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Create a label for the title
        ttk.Label(self.container, text="Database Records and Profile Creator", font=("Arial", 16)).pack(pady=10)

        # Initialize the database connection first
        self.conn = sqlite3.connect("profiles.db")
        self.create_table()  # Create the table if it doesn't exist

        # Fetch and display the data from the database
        self.display_data()

        # Add menu for profile creation and database actions
        self.create_menu()

        # Create buttons for database actions
        self.create_buttons()

    def create_table(self):
        """Creates the table in the database if it doesn't exist."""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profiles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname TEXT,
                middlename TEXT,
                lastname TEXT,
                age TEXT,
                dob TEXT,
                phone_numbers TEXT,
                emails TEXT,
                cars_and_plates TEXT
            )
        ''')
        self.conn.commit()

    def display_data(self):
        """Fetches and displays data from the database in a Treeview."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM profiles")
        records = cursor.fetchall()

        # Create a Treeview widget to display the data
        self.treeview = ttk.Treeview(self.container, columns=("ID", "Firstname", "Middlename", "Lastname", "Age", "DOB", "Phone", "Email", "Cars & Plates"), show="headings")
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Define column headings
        for col in self.treeview["columns"]:
            self.treeview.heading(col, text=col)

        # Insert the fetched data into the Treeview
        for record in records:
            self.treeview.insert("", "end", values=record)

    def create_menu(self):
        """Creates a menu bar with options for profile creation."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Create a 'File' menu with options to create a profile
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Create Profile", command=self.create_profile)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_buttons(self):
        """Creates buttons for performing database actions."""
        # Create a button frame
        button_frame = ttk.Frame(self.container)
        button_frame.pack(pady=20)

        # Create buttons for database actions
        ttk.Button(button_frame, text="Add Record", command=self.add_record).grid(row=0, column=0, padx=10)
        ttk.Button(button_frame, text="Delete Record", command=self.delete_record).grid(row=0, column=1, padx=10)

    def create_profile(self):
        """Creates a dialog to input profile data."""
        profile_window = tk.Toplevel(self.root)
        profile_window.title("Create Profile")

        # Create input fields for profile data
        ttk.Label(profile_window, text="First Name").grid(row=0, column=0, padx=10, pady=5)
        first_name_entry = ttk.Entry(profile_window)
        first_name_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Middle Name").grid(row=1, column=0, padx=10, pady=5)
        middle_name_entry = ttk.Entry(profile_window)
        middle_name_entry.grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Last Name").grid(row=2, column=0, padx=10, pady=5)
        last_name_entry = ttk.Entry(profile_window)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Age").grid(row=3, column=0, padx=10, pady=5)
        age_entry = ttk.Entry(profile_window)
        age_entry.grid(row=3, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Date of Birth").grid(row=4, column=0, padx=10, pady=5)
        dob_entry = ttk.Entry(profile_window)
        dob_entry.grid(row=4, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Phone Numbers").grid(row=5, column=0, padx=10, pady=5)
        phone_entry = ttk.Entry(profile_window)
        phone_entry.grid(row=5, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Emails").grid(row=6, column=0, padx=10, pady=5)
        email_entry = ttk.Entry(profile_window)
        email_entry.grid(row=6, column=1, padx=10, pady=5)

        ttk.Label(profile_window, text="Cars and Plates").grid(row=7, column=0, padx=10, pady=5)
        cars_entry = ttk.Entry(profile_window)
        cars_entry.grid(row=7, column=1, padx=10, pady=5)

        # Submit button to save profile data
        def submit_profile():
            # Insert the profile data into the database
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO profiles (firstname, middlename, lastname, age, dob, phone_numbers, emails, cars_and_plates)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (first_name_entry.get(), middle_name_entry.get(), last_name_entry.get(), age_entry.get(), dob_entry.get(), phone_entry.get(), email_entry.get(), cars_entry.get()))
            self.conn.commit()

            # Refresh the displayed data
            self.display_data()

            profile_window.destroy()

        ttk.Button(profile_window, text="Submit", command=submit_profile).grid(row=8, columnspan=2, pady=20)

    def add_record(self):
        """Simple implementation for adding a dummy record."""
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO profiles (firstname, middlename, lastname, age, dob, phone_numbers, emails, cars_and_plates)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ("John", "Doe", "Smith", "30", "1993-04-15", "123-456-7890", "johndoe@example.com", "ABC123, XYZ789"))
        self.conn.commit()
        self.display_data()

    def delete_record(self):
        """Deletes the selected record from the database."""
        selected_item = self.treeview.selection()
        if selected_item:
            record_id = self.treeview.item(selected_item[0], "values")[0]
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM profiles WHERE id=?", (record_id,))
            self.conn.commit()
            self.treeview.delete(selected_item)

# Initialize the tkinter window
root = tk.Tk()
app = DatabaseApp(root)

# Start the main loop
root.mainloop()
