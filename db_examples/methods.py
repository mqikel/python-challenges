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
    return {}

# Create a method to find a task into db
def filter_by_done(task_title:str):
    pass

# Delete
def delete_by_titile(task_title:str) -> bool:
    return False

# Update task
def update_task(modify_task:dict) -> dict:
    return {}

# Show all db registry
def show_all_db():
    print(DB)
