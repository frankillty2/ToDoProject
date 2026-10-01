tasks = []

def add_task(task):
    tasks.append(task)

def show_tasks():
    for number, task in enumerate (tasks, 1):
        print(f"{number}. {task}")

add_task("Вивчити Git")
add_task("Створити репозиторий")
show_tasks()