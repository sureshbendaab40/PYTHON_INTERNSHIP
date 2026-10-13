"""
Contact Management System - Medium-Level Version
--------------------------------------------------
Improvements over the basic version:
- Object-Oriented Design (Contact + ContactManager classes)
- Persistent storage using JSON file (data survives after closing)
- Input validation (phone number, email format) using regex
- Duplicate detection
- Sorting contacts alphabetically
- Proper exception handling
- Unique contact IDs
"""

import json
import os
import re


DATA_FILE = "contacts_data.json"


class Contact:
    """Represents a single contact."""

    def __init__(self, contact_id, name, phone, email):
        self.contact_id = contact_id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.contact_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @staticmethod
    def from_dict(data):
        return Contact(data["id"], data["name"], data["phone"], data["email"])

    def __str__(self):
        return f"[{self.contact_id}] {self.name} | 📞 {self.phone} | ✉ {self.email}"


class ContactManager:
    """Handles all operations: add, view, search, update, delete, save, load."""

    def __init__(self, filename=DATA_FILE):
        self.filename = filename
        self.contacts = []
        self.next_id = 1
        self.load_contacts()

    # ---------- Validation helpers ----------
    @staticmethod
    def is_valid_phone(phone):
        return re.fullmatch(r"\d{10}", phone) is not None

    @staticmethod
    def is_valid_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.fullmatch(pattern, email) is not None

    # ---------- File persistence ----------
    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    data = json.load(f)
                    self.contacts = [Contact.from_dict(c) for c in data]
                    if self.contacts:
                        self.next_id = max(c.contact_id for c in self.contacts) + 1
            except (json.JSONDecodeError, IOError) as e:
                print(f"Warning: Could not load contacts file ({e}). Starting fresh.")
                self.contacts = []
        else:
            self.contacts = []

    def save_contacts(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([c.to_dict() for c in self.contacts], f, indent=4)
        except IOError as e:
            print(f"Error saving contacts: {e}")

    # ---------- Core operations ----------
    def add_contact(self, name, phone, email):
        if not name:
            raise ValueError("Name cannot be empty.")
        if not self.is_valid_phone(phone):
            raise ValueError("Phone number must be exactly 10 digits.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")

        # Duplicate check (same name + phone)
        for c in self.contacts:
            if c.name.lower() == name.lower() and c.phone == phone:
                raise ValueError("A contact with this name and phone already exists.")

        contact = Contact(self.next_id, name, phone, email)
        self.contacts.append(contact)
        self.next_id += 1
        self.save_contacts()
        return contact

    def view_all(self, sort_by_name=True):
        if not self.contacts:
            return []
        result = self.contacts.copy()
        if sort_by_name:
            result.sort(key=lambda c: c.name.lower())
        return result

    def search(self, keyword):
        keyword = keyword.lower()
        return [
            c for c in self.contacts
            if keyword in c.name.lower()
            or keyword in c.phone
            or keyword in c.email.lower()
        ]

    def get_by_id(self, contact_id):
        for c in self.contacts:
            if c.contact_id == contact_id:
                return c
        return None

    def update_contact(self, contact_id, name=None, phone=None, email=None):
        contact = self.get_by_id(contact_id)
        if not contact:
            raise ValueError(f"No contact found with ID {contact_id}.")

        if name:
            contact.name = name
        if phone:
            if not self.is_valid_phone(phone):
                raise ValueError("Phone number must be exactly 10 digits.")
            contact.phone = phone
        if email:
            if not self.is_valid_email(email):
                raise ValueError("Invalid email format.")
            contact.email = email

        self.save_contacts()
        return contact

    def delete_contact(self, contact_id):
        contact = self.get_by_id(contact_id)
        if not contact:
            raise ValueError(f"No contact found with ID {contact_id}.")
        self.contacts.remove(contact)
        self.save_contacts()
        return contact


# ---------------- Console Interface ----------------
def print_menu():
    print("\n===== Contact Management System (Medium Level) =====")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    manager = ContactManager()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                name = input("Name: ").strip()
                phone = input("Phone (10 digits): ").strip()
                email = input("Email: ").strip()
                contact = manager.add_contact(name, phone, email)
                print(f"Added: {contact}")

            elif choice == "2":
                all_contacts = manager.view_all()
                if not all_contacts:
                    print("No contacts saved yet.")
                else:
                    print("\n--- All Contacts ---")
                    for c in all_contacts:
                        print(c)

            elif choice == "3":
                keyword = input("Enter name/phone/email to search: ").strip()
                results = manager.search(keyword)
                if results:
                    print("\n--- Search Results ---")
                    for c in results:
                        print(c)
                else:
                    print("No matching contacts found.")

            elif choice == "4":
                cid = int(input("Enter contact ID to update: ").strip())
                print("Leave a field blank to keep it unchanged.")
                name = input("New name: ").strip() or None
                phone = input("New phone: ").strip() or None
                email = input("New email: ").strip() or None
                contact = manager.update_contact(cid, name, phone, email)
                print(f"Updated: {contact}")

            elif choice == "5":
                cid = int(input("Enter contact ID to delete: ").strip())
                contact = manager.delete_contact(cid)
                print(f"Deleted: {contact}")

            elif choice == "6":
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1-6.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
