from methods import create_task
from methods import save_task
from methods import show_all_db
from methods import find_task

new_task = create_task("Tarea 1")
save_task(new_task)

task_2 = create_task("Tarea 2")
save_task(task_2)

print(find_task("Tarea 2"))
# show_all_db()