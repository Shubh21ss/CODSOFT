import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def show_all(contacts):
    if not contacts:
        print("\n  No contacts found!")
        return
    print("\n  ╔════╦══════════════════════╦═════════════════╗")
    print("  ║ No ║ Name                 ║ Phone           ║")
    print("  ╠════╬══════════════════════╬═════════════════╣")
    for i, c in enumerate(contacts, 1):
        name = c['name'][:20]
        phone = c['phone'][:15]
        print(f"  ║ {i:<2} ║ {name:<20} ║ {phone:<15} ║")
    print("  ╚════╩══════════════════════╩═════════════════╝")

def show_details(c):
    print("\n  ┌───────────────────────────┐")
    print(f"  │ Name  : {c['name']:<23} │")
    print(f"  │ Phone : {c['phone']:<23} │")
    print("  └───────────────────────────┘")

def add_contact(contacts):
    print("\n  --- ADD NEW CONTACT ---")
    name  = input("  Name    : ").strip()
    phone = input("  Phone   : ").strip()

    if not name or not phone:
        print("  ⚠ Name and phone are required!")
        return

    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print(f"  ✔ Contact '{name}' added!")

def search_contact(contacts):
    query = input("\n  Search by name or phone: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if results:
        print(f"\n  Found {len(results)} result(s):")
        for c in results:
            show_details(c)
    else:
        print("  No matching contacts found.")

def update_contact(contacts):
    show_all(contacts)
    try:
        num = int(input("\n  Enter contact number to update: "))
        if 1 <= num <= len(contacts):
            c = contacts[num - 1]
            print(f"  Updating: {c['name']} (press Enter to keep current value)")
            name  = input(f"  Name    [{c['name']}]   : ").strip()
            phone = input(f"  Phone   [{c['phone']}]  : ").strip()

            if name:  c['name']  = name
            if phone: c['phone'] = phone

            save_contacts(contacts)
            print("  ✔ Contact updated!")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def delete_contact(contacts):
    show_all(contacts)
    try:
        num = int(input("\n  Enter contact number to delete: "))
        if 1 <= num <= len(contacts):
            removed = contacts.pop(num - 1)
            save_contacts(contacts)
            print(f"  ✔ Contact '{removed['name']}' deleted!")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def main():
    print("\n  ====================================")
    print("      CODSOFT - CONTACT BOOK APP     ")
    print("  ====================================")
    contacts = load_contacts()

    while True:
        print("\n  MENU:")
        print("  1. View All Contacts")
        print("  2. Add Contact")
        print("  3. Search Contact")
        print("  4. Update Contact")
        print("  5. Delete Contact")
        print("  6. Exit")

        choice = input("\n  Choose an option (1-6): ").strip()

        if choice == "1":
            show_all(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\n  Goodbye! Stay connected! 👋\n")
            break
        else:
            print("  Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
