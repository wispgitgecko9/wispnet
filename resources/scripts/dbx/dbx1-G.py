#####################################################
#WISPNET dbx Model 1-Graphical | Created 12.17.2024 #
#####################################################

import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class UserProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WISPNET Profile Creator")

        self.user_data = {
            "name": {},
            "age": None,
            "dob": None,
            "phone_numbers": [],
            "emails": [],
            "cars_and_plates": []
        }

        self.intro_label = tk.Label(root, text=(
            "Welcome to WISPNET experimental network!\n"
            "This GUI will guide you to create a profile based on your input."
        ), padx=10, pady=10)
        self.intro_label.pack()

        self.start_button = tk.Button(root, text="Start", command=self.fileinfo)
        self.start_button.pack(pady=10)

    def fileinfo(self):
        self.user_data["filename"] = simpledialog.askstring(
            "File Information", "Enter your full name in the format [LAST_FIRST]:"
        )
        if not self.user_data["filename"]:
            messagebox.showerror("Input Error", "Filename cannot be empty.")
            return
        self.nameinfo()

    def nameinfo(self):
        self.user_data["name"]["first"] = simpledialog.askstring("Name", "Enter your first name:")
        self.user_data["name"]["middle"] = simpledialog.askstring("Name", "Enter your middle name:")
        self.user_data["name"]["last"] = simpledialog.askstring("Name", "Enter your last name:")
        self.ageinfo()

    def ageinfo(self):
        try:
            self.user_data["age"] = int(simpledialog.askstring("Age", "Enter your age:"))
        except ValueError:
            messagebox.showerror("Input Error", "Age must be a number.")
            return
        self.dobinfo()

    def dobinfo(self):
        dob = simpledialog.askstring(
            "Date of Birth",
            f"What is {self.user_data['name']['first']} {self.user_data['name']['last']}'s Date of Birth?\nEnter in mmm/dd/yy format."
        )
        try:
            self.user_data["dob"] = datetime.strptime(dob, "%b/%d/%y")
        except ValueError:
            messagebox.showerror("Input Error", "Invalid date format. Please try again.")
            return self.dobinfo()
        self.numbercontactinfo()

    def numbercontactinfo(self):
        if messagebox.askyesno("Phone Numbers", "Are there any phone numbers associated?"):
            count = simpledialog.askinteger("Phone Numbers", "How many phone numbers?")
            for i in range(count):
                number = simpledialog.askstring("Phone Number", f"Enter phone number {i + 1}:")
                self.user_data["phone_numbers"].append(number)
        self.emailcontactinfo()

    def emailcontactinfo(self):
        if messagebox.askyesno("Emails", "Are there any emails associated?"):
            count = simpledialog.askinteger("Emails", "How many emails?")
            for i in range(count):
                email = simpledialog.askstring("Email", f"Enter email {i + 1}:")
                self.user_data["emails"].append(email)
        self.plateinfo()

    def plateinfo(self):
        if messagebox.askyesno("License Plates", "Are there any license plates associated?"):
            count = simpledialog.askinteger("License Plates", "How many license plates?")
            for i in range(count):
                car_make = simpledialog.askstring("Car Info", f"Enter car make for plate {i + 1}:")
                car_model = simpledialog.askstring("Car Info", f"Enter car model for plate {i + 1}:")
                plate_number = simpledialog.askstring("Car Info", f"Enter license plate number {i + 1}:")
                self.user_data["cars_and_plates"].append({
                    "make": car_make,
                    "model": car_model,
                    "plate": plate_number
                })
        self.profcheck()

    def profcheck(self):
        summary = (
            f"NAME: {self.user_data['name']['first']} {self.user_data['name']['middle']} {self.user_data['name']['last']}\n"
            f"Age: {self.user_data['age']}\n"
            f"Date of Birth: {self.user_data['dob'].strftime('%B %d, %Y')}\n"
            f"Phone Numbers: {', '.join(self.user_data['phone_numbers'])}\n"
            f"Emails: {', '.join(self.user_data['emails'])}\n"
            f"Cars and Plates:\n"
        )

        for i, car in enumerate(self.user_data["cars_and_plates"], start=1):
            summary += f"  {i}. {car['make']} {car['model']} - {car['plate']}\n"

        if messagebox.askyesno("Confirm", f"Does this information look correct?\n\n{summary}"):
            self.filecreate()
        else:
            messagebox.showinfo("Restart", "Please restart the program to re-enter the information.")

    def filecreate(self):
        filename = f"{self.user_data['filename']}.txt"
        with open(filename, "w") as file:
            file.write(f"NAME: {self.user_data['name']['first']} {self.user_data['name']['middle']} {self.user_data['name']['last']}\n")
            file.write(f"Age: {self.user_data['age']}\n")
            file.write(f"Date of Birth: {self.user_data['dob'].strftime('%B %d, %Y')}\n")
            file.write("Phone Numbers:\n")
            for number in self.user_data["phone_numbers"]:
                file.write(f"  - {number}\n")
            file.write("Emails:\n")
            for email in self.user_data["emails"]:
                file.write(f"  - {email}\n")
            file.write("Cars and Plates:\n")
            for car in self.user_data["cars_and_plates"]:
                file.write(f"  - {car['make']} {car['model']} - {car['plate']}\n")
        messagebox.showinfo("File Created", f"Registry complete. File created: {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = UserProfileApp(root)
    root.mainloop()
