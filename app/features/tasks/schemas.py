from pydantic import BaseModel

#Pydantic schemas
class TaskBase(BaseModel):
    title: str

class TaskCreate(TaskBase):
    pass

class TaskOut(TaskBase):
    id: int

    class Config:
        from_attributes = True