tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for number, task in enumerate (tasks, 1):
        print(f"{number}. {task}")

def delete_task(number):
    if 1 <= number <= len(tasks):
        tasks.pop(number - 1)

add_task("Вивчити Git")
add_task("Створити репозиторій")
show_tasks()

def search_task(keyword):
    found = [task for task in tasks if keyword.lower() in task.lower()]
    for task in found:
        print(f"Знайдено: {task}")