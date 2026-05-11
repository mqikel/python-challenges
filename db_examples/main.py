from methods import create_task, save_task, show_all_db, find_task_by_title, filter_by_done, delete_by_title

task_1 = create_task("Tarea 1")
save_task(task_1)
task_2 = create_task("Tarea 2")
save_task(task_2)
task_3 = create_task("Tarea 3")
save_task(task_3)
task_4 = create_task("Tarea 4")
save_task(task_4)

task_3["done"] = True
task_1["done"] = True
show_all_db()
print(find_task_by_title("Tarea 3"))
print(filter_by_done())
delete_by_title("Tarea 1")
print(filter_by_done())


# print(find_task_by_title("Tarea 2"))
# show_all_db()
# Example update
# task_2_update = task_2.copy()
# task_2_update["description"] = "This is the second task"
# task_2_update["done"] = True
# update_task(task_2_update)