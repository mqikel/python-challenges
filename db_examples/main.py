from methods import create_task
from methods import save_task
from methods import show_all_db

new_task = create_task("Tarea 1")
save_task(new_task)

task_2 = create_task("Tarea 2")
save_task(task_2)

# print(find_task("Tarea 2"))
show_all_db()


# Example update
task_2_update = task_2.copy()
task_2_update["description"] = "This is the second task"
task_2_update["done"] = True
update_task(task_2_update)