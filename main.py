#import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

#Initiate it
app =FastAPI()

#Initialize empty task list
tasks = []

#Define the root endpoint
@app.get("/")
def read_root():
    return{"Hello": "World"}

#Define the task model
class Task(BaseModel):
    id: Optional[int] = None
    description: str