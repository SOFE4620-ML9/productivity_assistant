from agent import parse_task_from_input
from task_manager import add_task, load_tasks, delete_task


def main():
    print("🤖 Welcome to Smart TaskBot!")
    while True:
        print("\nOptions: [1] Add Task [2] View Tasks [3] Delete Task [4] Exit")
        choice = input("Your choice: ")

        if choice == '1':
            user_input = input("Enter a task (e.g., 'Remind me to email prof tomorrow'): ")
            parsed = parse_task_from_input(user_input)
            if parsed:
                print("✅ Parsed Task:")
                print(parsed)
                confirm = input("Add this task? (y/n): ")
                if confirm.lower() == 'y':
                    add_task(parsed)
                    print("✅ Task added!")
            else:
                print("❌ Couldn't understand your input.")

        elif choice == '2':
            tasks = load_tasks()
            if not tasks:
                print("📭 No tasks yet.")
            else:
                for idx, task in enumerate(tasks):
                    print(f"{idx + 1}. {task['task']} - {task.get('date')} at {task.get('time')}")

        elif choice == '3':
            tasks = load_tasks()
            for idx, task in enumerate(tasks):
                print(f"{idx + 1}. {task['task']}")
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
            print("🗑️ Task deleted!")

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❓ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
