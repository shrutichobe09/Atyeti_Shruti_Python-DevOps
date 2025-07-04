from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str
  
class TaskOut(TaskCreate):
    id: int
    completed: bool

    class Config:
        orm_mode = True
