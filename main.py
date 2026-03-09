#import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#Initiate it
app =FastAPI()

#Initialize empty task list
tasks = []

#Define the task model
class Task(BaseModel):
    id: Optional[int] = None
    description: str

#Define the root endpoint
@app.get("/")
def read_root():
    return{"Hello": "World"}

#Create endpoint
@app.post("/task")
def create_task(task: Task):
    tasks.append(task.dict())
    return tasks[-1]

#Read endpoint
@app.get("/task/{task_id}")
def read_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            return task
        
#Update endpoint
@app.put("/task/{task_id}")
def update_task(task_id: int, new_task: Task):
    for task in tasks:
        if task['id'] == task_id:
            task.update(new_task.dict())
            return task

#Delete endpoint
@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return task