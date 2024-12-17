#####################################################
#WISPNET dbx Model 1-Alpha     | Created 12.17.2024 #
#####################################################

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile Creator")

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

        summary_text = f"Name: {self.data['firstname'].get() or ''} {self.data['middlename'].get() or ''} {self.data['lastname'].get() or ''}\n"
        summary_text += f"Age: {self.data['age'].get() or ''}\n"
        summary_text += f"DOB: {self.data['dob'].get() or ''}\n"
        summary_text += "Phone Numbers: " + ", ".join(filter(None, self.data["phone_numbers"])) + "\n"
        summary_text += "Emails: " + ", ".join(filter(None, self.data["emails"])) + "\n"
        summary_text += "Cars and Plates:\n"
        for car in self.data["cars_and_plates"]:
            summary_text += f"  - {car.get('Make', '')} {car.get('Model', '')}, Plate: {car.get('Plate', '')}\n"

        ttk.Label(self.container, text=summary_text, justify=tk.LEFT).pack(pady=10)

        ttk.Button(self.container, text="Save & Finish", command=self.save_and_exit).pack(pady=20)
        ttk.Button(self.container, text="Back", command=self.prev_step).pack(pady=5)

    def add_list_section(self, title, data_list, fields=None):
        section_frame = ttk.Frame(self.container)
        section_frame.pack(fill=tk.BOTH, pady=5)

        ttk.Label(section_frame, text=title + ":", font=("Arial", 12)).pack(anchor=tk.W)

        listbox = tk.Listbox(section_frame, height=5)
        listbox.pack(fill=tk.X, pady=5)
        for item in data_list:
            listbox.insert(tk.END, ", ".join(item.values() if fields else [item]))

        def add_item():
          if fields:
              new_item = {field: (simpledialog.askstring("Input", f"Enter {field}:") or "") for field in fields}
              data_list.append(new_item)
          else:
              new_item = simpledialog.askstring("Input", f"Enter {title[:-1]}:") or ""
              data_list.append(new_item)
          listbox.insert(tk.END, ", ".join(new_item.values() if fields else [new_item]))


        ttk.Button(section_frame, text="Add", command=add_item).pack()

    def nav_buttons(self):
        button_frame = ttk.Frame(self.container)
        button_frame.pack(fill=tk.X, pady=10)

        if self.current_step > 0:
            ttk.Button(button_frame, text="Back", command=self.prev_step).pack(side=tk.LEFT)

        ttk.Button(button_frame, text="Next", command=self.next_step).pack(side=tk.RIGHT)

    def save_and_exit(self):
       filepath = f"{self.data['firstname'].get() or 'Unnamed'}_{self.data['lastname'].get() or 'Profile'}.txt"
       try:
            with open(filepath, "w") as file:
                file.write(f"Name: {self.data['firstname'].get() or ''} {self.data['middlename'].get() or ''} {self.data['lastname'].get() or ''}\n")
                file.write(f"Age: {self.data['age'].get() or ''}\n")
            file.write(f"DOB: {self.data['dob'].get() or ''}\n")
            file.write("Phone Numbers:\n")
            for number in filter(None, self.data["phone_numbers"]):
                  file.write(f"  - {number}\n")
            file.write("Emails:\n")
            for email in filter(None, self.data["emails"]):
                  file.write(f"  - {email}\n")
            file.write("Cars and Plates:\n")
            for car in self.data["cars_and_plates"]:
                  file.write(f"  - {car.get('Make', '')} {car.get('Model', '')}, Plate: {car.get('Plate', '')}\n")
            messagebox.showinfo("Success", f"Profile saved to {filepath}.")
       except Exception as e:
          messagebox.showerror("Error", f"Failed to save profile: {e}")
       self.root.destroy()


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
