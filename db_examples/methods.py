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
    title = {
    "done": False,
    "title": "",
    "description": "",
    "comentaries": [],
    "due_date": "",
    "files": [],
    "requirement": []
    }
    return title

# Create a method to save task into db
def save_task(task:dict):
    DB.append(task)

# Create a method to find a task into db

def find_task(task:dict):
    if task in DB:
        return task
    else: 
        return False

# Show all db registry
def show_all_db():
    print(DB)
