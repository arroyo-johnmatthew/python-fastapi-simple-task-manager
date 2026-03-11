from sqlalchemy.orm import Session
from typing import List, Optional
from app.features.tasks.models import Task
from app.features.tasks.schemas import TaskCreate

# CRUD functions (no endpoints)

#Create a task
def create_task(task: TaskCreate, db: Session) -> Task:
    db_task = Task(title=task.title)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# Read all tasks
def get_tasks(db: Session) -> List[Task]:
    return db.query(Task).all()

# Read a single task
def get_task(task_id: int, db: Session) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()
    
# Update a task
def update_task(task_id: int, task_update: TaskCreate, db: Session) -> Optional[Task]:
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task:
        task.title = task_update.title
        db.commit()
        db.refresh(task)
        return task

# Delete a task
def delete_task(task_id: int, db: Session) -> bool:
    task = db.query(Task).filter(Task.id == task_id).first()
    
    if task:
        db.delete(task)
        db.commit()
        return True
    return False