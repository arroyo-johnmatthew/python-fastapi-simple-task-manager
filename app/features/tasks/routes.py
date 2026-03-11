from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from .crud import create_task, get_tasks, get_task, update_task, delete_task
from schemas import TaskCreate, TaskOut

router = APIRouter()

# Router endpoints
# Create task endpoint
@router.post("/tasks/", response_model=TaskOut)
def create_task_endpoint(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(task, db)

# Get all tasks endpoint
@router.get("/tasks/", response_model=List[TaskOut])
def get_tasks_endpoint(db: Session = Depends(get_db)):
    return get_tasks(db)

# Get a specific task endpoint
@router.get("/tasks/{task_id}", response_model=TaskOut)
def get_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = get_task(task_id, db)
    
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update task endpoint
@router.put("/tasks/{task_id}", response_model=TaskOut)
def update_task_endpoint(task_id: int, task_update: TaskCreate, db: Session = Depends(get_db)):
    updated_task = update_task(task_id, task_update, db)
    
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

# Delete task endpoint
@router.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task(task_id, db)

    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully🎉🎉"}



