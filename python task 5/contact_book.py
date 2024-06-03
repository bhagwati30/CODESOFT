import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.geometry("500x400")  # Set the window size to 500x400

        self.contacts = {}  # Dictionary to store contacts

        self.setup_ui()

    def setup_ui(self):
        # Setup the UI components with padding
        self.name_label = tk.Label(self.root, text="Name:", font=("Arial", 12))
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.name_entry = tk.Entry(self.root, font=("Arial", 12))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.phone_label = tk.Label(self.root, text="Phone Number:", font=("Arial", 12))
        self.phone_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.phone_entry = tk.Entry(self.root, font=("Arial", 12))
        self.phone_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 12))
        self.email_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.email_entry = tk.Entry(self.root, font=("Arial", 12))
        self.email_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.address_label = tk.Label(self.root, text="Address:", font=("Arial", 12))
        self.address_label.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.address_entry = tk.Entry(self.root, font=("Arial", 12))
        self.address_entry.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact, font=("Arial", 12))
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.view_button = tk.Button(self.root, text="View Contact List", command=self.view_contacts, font=("Arial", 12))
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(self.root, text="Search by Name or Phone:", font=("Arial", 12))
        self.search_label.grid(row=6, column=0, padx=10, pady=10, sticky=tk.W)
        self.search_entry = tk.Entry(self.root, font=("Arial", 12))
        self.search_entry.grid(row=6, column=1, padx=10, pady=10, sticky=tk.W)
        self.search_button = tk.Button(self.root, text="Search Contact", command=self.search_contact, font=("Arial", 12))
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact, font=("Arial", 12))
        self.update_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact, font=("Arial", 12))
        self.delete_button.grid(row=9, column=0, columnspan=2, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts[phone] = {"Name": name, "Email": email, "Address": address}
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone Number are required.")

    def view_contacts(self):
        contacts_list = tk.Toplevel(self.root)
        contacts_list.title("Contact List")
        contacts_list.geometry("300x400")

        row = 0
        for phone, details in self.contacts.items():
            tk.Label(contacts_list, text=f"{details['Name']} - {phone}", font=("Arial", 12)).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
            row += 1

    def search_contact(self):
        search_term = self.search_entry.get()
        if search_term:
            for phone, details in self.contacts.items():
                if search_term.lower() in details['Name'].lower() or search_term in phone:
                    self.name_entry.delete(0, tk.END)
                    self.phone_entry.delete(0, tk.END)
                    self.email_entry.delete(0, tk.END)
                    self.address_entry.delete(0, tk.END)

                    self.name_entry.insert(0, details['Name'])
                    self.phone_entry.insert(0, phone)
                    self.email_entry.insert(0, details['Email'])
                    self.address_entry.insert(0, details['Address'])
                    return
            messagebox.showinfo("Not Found", "Contact not found.")
        else:
            messagebox.showerror("Error", "Enter a name or phone number to search.")

    def update_contact(self):
        phone = self.phone_entry.get()
        if phone in self.contacts:
            self.contacts[phone] = {
                "Name": self.name_entry.get(),
                "Email": self.email_entry.get(),
                "Address": self.address_entry.get()
            }
            messagebox.showinfo("Success", "Contact updated successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        phone = self.phone_entry.get()
        if phone in self.contacts:
            del self.contacts[phone]
            messagebox.showinfo("Success", "Contact deleted successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Contact not found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
