MODEL_TASK = {
    "done": False,
    "title": "",
    "description": "",
    "comentaries": [],
    "due_date": "",
    "files": [],
    "requirement": []
}

DB = []

# Create a method that creates a task

def create_task(title:str) -> dict:
    new_task = {
        "done": False,
        "title": title,
        "description": "",
        "comentaries": [],
        "due_date": "",
        "files": [],
        "requirement": []
    }
    return new_task

# Create a method to save task into db
def save_task(task:dict):
    DB.append(task)

# Create a method to find a task into db
def find_task_by_title(task_title:str) -> dict:
    for task in DB:
        if task["title"] == task_title:
            return task
    return None

# Create a method to find a task into db
def filter_by_done() -> list:
    """
    Filters all tasks that have been done ("done": True)
    """
    done_task = []
    for task in DB:
        if task["done"] == True:
            done_task.append(task)
    return done_task
   

# Delete
def delete_by_title(task_title:str) -> bool:           
    for task in DB:
        if task["title"] == task_title:
            DB.remove(task)
            return True
    return False



# Update task
def update_task(modify_task:dict) -> dict:
    pass

# Show all db registry
def show_all_db():
    for task in DB:
        print(task)