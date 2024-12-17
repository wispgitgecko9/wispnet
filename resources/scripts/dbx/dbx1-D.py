#####################################################
#WISPNET dbx Model 1-Delta     | Created 12.17.2024 #
#####################################################

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import webbrowser

class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile Creator")

        # Create a menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # Add "Search" menu
        search_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Search", menu=search_menu)
        search_menu.add_command(label="Search by ID", command=self.search_by_id)

        # Create widgets (menu, buttons, etc.)
        self.create_widgets()

        # Database setup
        self.conn = sqlite3.connect("profiles.db")
        self.create_table()

        # Initialize variables
        self.data = {
            "firstname": tk.StringVar(),
            "middlename": tk.StringVar(),
            "lastname": tk.StringVar(),
            "age": tk.StringVar(),
            "dob": tk.StringVar(),
            "phone_numbers": [],
            "emails": [],
            "cars_and_plates": []
        }

        self.current_step = 0

        # Create main container
        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Initialize steps
        self.steps = [
            self.step_intro,
            self.step_nameinfo,
            self.step_ageinfo,
            self.step_dobinfo,
            self.step_contactinfo,
            self.step_carinfo,
            self.step_summary
        ]

        # Start first step
        self.steps[self.current_step]()

    def create_widgets(self):
        """Create and display the widgets (buttons, menu, etc.)."""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Add a "Profile" menu
        profile_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Profile", menu=profile_menu)
        profile_menu.add_command(label="Create Profile", command=self.create_profile)
        profile_menu.add_command(label="Search by ID", command=self.search_by_id)

        # Add a "Help" menu
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="Go to Site", command=self.open_site)
        help_menu.add_command(label="Go to Forum", command=self.open_forum)
        help_menu.add_command(label="Contact Support", command=self.contact_support)

    def open_site(self):
        webbrowser.open("http://wisp.wispnet.org/dbx")

    def open_forum(self):
        webbrowser.open("https://www.reddit.com/r/wispnet")

    def contact_support(self):
        webbrowser.open("mailto:help@wispnet.org")

    def search_by_id(self):
        """Search for a profile by ID and display the results."""
        profile_id = simpledialog.askinteger("Search by ID", "Enter the profile ID:")
        if profile_id is None:
            return  # User cancelled

        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM profiles WHERE id = ?", (profile_id,))
        result = cursor.fetchone()

        if result:
            # Display profile information
            profile_text = (
                f"ID: {result[0]}\n"
                f"Name: {result[1]} {result[2]} {result[3]}\n"
                f"Age: {result[4]}\n"
                f"DOB: {result[5]}\n"
                f"Phone Numbers: {result[6]}\n"
                f"Emails: {result[7]}\n"
                f"Cars and Plates: {result[8]}\n"
            )
            messagebox.showinfo("Profile Found", profile_text)
        else:
            messagebox.showerror("Not Found", f"No profile found with ID {profile_id}.")

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

    def create_profile(self):
        """Handle profile creation (step-by-step form)."""
        self.current_step = 0
        self.clear_container()
        self.steps[self.current_step]()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def next_step(self):
        self.current_step += 1
        self.clear_container()
        self.steps[self.current_step]()

    def prev_step(self):
        self.current_step -= 1
        self.clear_container()
        self.steps[self.current_step]()

    def step_intro(self):
        ttk.Label(self.container, text="Welcome to the Profile Creator!", font=("Arial", 16)).pack(pady=10)
        ttk.Label(self.container, text="You will be guided through a series of questions.").pack(pady=5)
        ttk.Button(self.container, text="Start", command=self.next_step).pack(pady=20)

    def step_nameinfo(self):
        ttk.Label(self.container, text="Enter your name information:", font=("Arial", 14)).pack(pady=10)

        ttk.Label(self.container, text="First Name:").pack(anchor=tk.W)
        ttk.Entry(self.container, textvariable=self.data["firstname"]).pack(fill=tk.X, pady=5)

        ttk.Label(self.container, text="Middle Name:").pack(anchor=tk.W)
        ttk.Entry(self.container, textvariable=self.data["middlename"]).pack(fill=tk.X, pady=5)

        ttk.Label(self.container, text="Last Name:").pack(anchor=tk.W)
        ttk.Entry(self.container, textvariable=self.data["lastname"]).pack(fill=tk.X, pady=5)

        self.nav_buttons()

    def step_ageinfo(self):
        ttk.Label(self.container, text="Enter your age:", font=("Arial", 14)).pack(pady=10)
        ttk.Entry(self.container, textvariable=self.data["age"]).pack(fill=tk.X, pady=5)
        self.nav_buttons()

    def step_dobinfo(self):
        ttk.Label(self.container, text="Enter your date of birth (MM/DD/YYYY):", font=("Arial", 14)).pack(pady=10)
        ttk.Entry(self.container, textvariable=self.data["dob"]).pack(fill=tk.X, pady=5)
        self.nav_buttons()

    def step_contactinfo(self):
        ttk.Label(self.container, text="Enter contact information:", font=("Arial", 14)).pack(pady=10)
        self.add_list_section("Phone Numbers", self.data["phone_numbers"])
        self.add_list_section("Emails", self.data["emails"])
        self.nav_buttons()

    def step_carinfo(self):
        ttk.Label(self.container, text="Enter car and plate information:", font=("Arial", 14)).pack(pady=10)
        self.add_list_section("Cars and Plates", self.data["cars_and_plates"], fields=["Make", "Model", "Plate"])
        self.nav_buttons()

    def step_summary(self):
        ttk.Label(self.container, text="Summary", font=("Arial", 16)).pack(pady=10)

        summary_text = f"Name: {self.data['firstname'].get()} {self.data['middlename'].get()} {self.data['lastname'].get()}\n"
        summary_text += f"Age: {self.data['age'].get()}\n"
        summary_text += f"DOB: {self.data['dob'].get()}\n"
        summary_text += "Phone Numbers: " + ", ".join(self.data["phone_numbers"]) + "\n"
        summary_text += "Emails: " + ", ".join(self.data["emails"]) + "\n"
        summary_text += "Cars and Plates:\n"
        for car in self.data["cars_and_plates"]:
            summary_text += f"  - {car['Make']} {car['Model']}, Plate: {car['Plate']}\n"

        ttk.Label(self.container, text=summary_text, justify=tk.LEFT).pack(pady=10)
        ttk.Button(self.container, text="Save & Finish", command=self.save_to_database).pack(pady=20)
        ttk.Button(self.container, text="Back", command=self.prev_step).pack(pady=5)

    def add_list_section(self, title, data_list, fields=None):
        section_frame = ttk.Frame(self.container)
        section_frame.pack(fill=tk.BOTH, pady=5)

        ttk.Label(section_frame, text=title + ":", font=("Arial", 12)).pack(anchor=tk.W)

        listbox = tk.Listbox(section_frame, height=5)
        listbox.pack(fill=tk.X, pady=5)
        for item in data_list:
            listbox.insert(tk.END, ", ".join(item.values() if fields else [item]))

    def add_item(self, title, data_list, fields=None):
        if fields:
            new_item = {field: simpledialog.askstring("Input", f"Enter {field}:") for field in fields}
            data_list.append(new_item)
            listbox.insert(tk.END, f"{new_item['Make']} {new_item['Model']} - Plate: {new_item['Plate']}")
        else:
            new_item = simpledialog.askstring("Input", f"Enter {title[:-1]}:")
            data_list.append(new_item)
            listbox.insert(tk.END, new_item)

            ttk.Button(section_frame, text="Add", command=lambda: self.add_item(title, data_list)).pack()

    def nav_buttons(self):
        button_frame = ttk.Frame(self.container)
        button_frame.pack(fill=tk.X, pady=10)
        if self.current_step > 0:
            ttk.Button(button_frame, text="Previous", command=self.prev_step).pack(side=tk.LEFT, padx=10)
        ttk.Button(button_frame, text="Next", command=self.next_step).pack(side=tk.RIGHT, padx=10)

    def save_to_database(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO profiles (firstname, middlename, lastname, age, dob, phone_numbers, emails, cars_and_plates)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.data["firstname"].get(),
            self.data["middlename"].get(),
            self.data["lastname"].get(),
            self.data["age"].get(),
            self.data["dob"].get(),
            ", ".join(self.data["phone_numbers"]),
            ", ".join(self.data["emails"]),
            ", ".join([f"{car['Make']} {car['Model']} ({car['Plate']})" for car in self.data["cars_and_plates"]])
        ))
        self.conn.commit()
        messagebox.showinfo("Success", "Profile saved successfully!")

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Help")

        # Help message
        help_text = "This application allows you to create and search profiles."
        ttk.Label(help_window, text=help_text).pack(pady=10)

        # Site button
        site_button = ttk.Button(help_window, text="Go to Site", command=lambda: webbrowser.open("http://wisp.wispnet.org/dbx"))
        site_button.pack(fill=tk.X, pady=5)

        # Forum button
        forum_button = ttk.Button(help_window, text="Go to Forum", command=lambda: webbrowser.open("https://www.reddit.com/r/wispnet"))
        forum_button.pack(fill=tk.X, pady=5)

        # Contact button
        contact_button = ttk.Button(help_window, text="Contact Support", command=lambda: webbrowser.open("mailto:help@wispnet.org"))
        contact_button.pack(fill=tk.X, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
