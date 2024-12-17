#####################################################
#WISPNET dbx Patch for dbx1-B  | Created 12.17.2024 #
#####################################################

import tkinter as tk
from tkinter import ttk
import sqlite3

class ProfileApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Database Viewer")

        # Create Treeview to display records
        self.tree = ttk.Treeview(root, columns=("ID", "Name", "Age"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Add a Delete Record button
        delete_button = ttk.Button(root, text="Delete Record", command=self.delete_record)
        delete_button.pack(pady=10)

        # Populate Treeview with data from the database
        self.display_data()

    def display_data(self):
        """Fetch and display data from the database."""
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()

        # Clear the Treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch data from the database
        cursor.execute("SELECT id, name, age FROM profiles")
        rows = cursor.fetchall()
        for row in rows:
            self.tree.insert("", "end", values=row)

        conn.close()

    def delete_record(self):
        """Delete the selected record from the database."""
        selected_item = self.tree.selection()
        if not selected_item:
            tk.messagebox.showerror("Error", "No record selected!")
            return

        # Get the ID of the selected record
        record = self.tree.item(selected_item)
        record_id = record["values"][0]

        # Delete the record from the database
        conn = sqlite3.connect("example.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM profiles WHERE id = ?", (record_id,))
        conn.commit()
        conn.close()

        # Refresh the display
        self.display_data()
        tk.messagebox.showinfo("Success", "Record deleted successfully!")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfileApp(root)
    root.mainloop()
