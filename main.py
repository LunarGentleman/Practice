import json
import os

tasks = []

def load_tasks():
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                global tasks
                tasks = json.load(file)
        except json.JSONDecodeError:
            tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task():
    description = input("Введите задачу: ").strip()
    if description:
        tasks.append({"Описание": description, "Выполнено": False})
        save_tasks()
        print("Задача успешно добавлена!")
    else:
        print("Задача не может быть пустой.")

def display_tasks():
    if not tasks:
        print("Нет доступных задач.")
        return
    # Сортировка: сначала невыполненные, потом выполненные 
    sorted_tasks = sorted(tasks, key=lambda x: x["Выполнено"])
    for i, task in enumerate(sorted_tasks, 1):
        status = "✔" if task["Выполнено"] else " "
        print(f"{i}. [{status}] {task['Описание']}")

def complete_task():
    display_tasks()
    try:
        index = int(input("Введите номер задачи, которую нужно отметить как выполненную: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["Выполнено"] = True
            save_tasks()
            print("Задача отмечена, как выполненная!")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите корректный номер задачи.")

def delete_task():
    display_tasks()
    try:
        index = int(input("Введите номер задачи для удаления: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            save_tasks()
            print("Задача успешно удалена!")
        else:
            print("Некорректный номер задачи.")
    except ValueError:
        print("Пожалуйста, введите корректный номер задачи.")

def main():
    load_tasks()
    while True:
        print("\nTodo List меню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу, как выполненную")
        print("4. Удалить задачу")
        print("5. Выйти")
        choice = input("Выберите опцию (1-5): ").strip()
        
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("До новыз встреч!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()