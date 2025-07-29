from database import setup_database, add_task, get_all_tasks, mark_task_completed

def show_menu():
    print("\n--- Aufgabenverwaltung ---")
    print("1. Neue Aufgabe hinzufügen")
    print("2. Alle Aufgaben anzeigen")
    print("3. Aufgabe als erledigt markieren")
    print("0. Beenden")

def main():
    setup_database()
    while True:
        show_menu()
        choice = input("Option auswählen: ")

        if choice == "1":
            title = input("Titel: ")
            description = input("Beschreibung: ")
            add_task(title, description)
            print("✅ Aufgabe hinzugefügt.")

        elif choice == "2":
            tasks = get_all_tasks()
            if not tasks:
                print("📭 Keine Aufgaben vorhanden.")
            else:
                for task in tasks:
                    print(task)

        elif choice == "3":
            task_id = input("ID der Aufgabe: ")
            if task_id.isdigit():
                mark_task_completed(int(task_id))
                print("🗸 Aufgabe als erledigt markiert.")
            else:
                print("⚠️ Ungültige ID.")

        elif choice == "0":
            print("Bis bald!")
            break

        else:
            print("Ungültige Auswahl.")

if __name__ == "__main__":
    main()
