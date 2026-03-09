import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Database configurations
SQLALCHEMY_DATABASE_URL = "sqlite:///./tasks.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# SQLAlchemy model (database table)
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

# Pydantic schemas (API validation)
class TaskBase(BaseModel):
    description: str
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int
    class Config:
        orm_mode = True

# FastAPI app instance
app = FastAPI()

# CRUD operations
@app.post("/tasks/", response_model=TaskOut)
def create_task(task: TaskCreate):
    db = SessionLocal()

    db_task = Task(description=task.description, completed=task.completed)
    db.add(db_task)         # stage the new record
    db.commit()             # append it to tasks.db
    db.refresh(db_task)     # fetch the auto-generated id

    return db_task

@app.get("/tasks/{task_id}", response_model=TaskOut)
def read_tasks(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")
    return task

@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_tasks(task_id: int, updated_task: TaskCreate):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")
    
    task.description = updated_task.description
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}", response_model=TaskOut)
def delete_tasks(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task Not Found")
    
    db.delete(task)
    db.commit()
    return task

if __name__ == "__main__":
    uvicorn.run(app)