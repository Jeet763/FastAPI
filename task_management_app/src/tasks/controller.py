from src.tasks.dtos import Taskschema
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
from fastapi import HTTPException

def create_task(body:Taskschema , db:Session):
    data = body.model_dump()
    new_task = TaskModel(title= data["title"] , 
                         description = data["description"],
                         is_completed = data["is_completed"]
                         )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
#     return {"status": "Task Created Successfully..." , "data": new_task}

def get_tasks(db:Session):
     tasks = db.query(TaskModel).all()
     return tasks

def get_one_task(task_id:int ,db:Session):
     one_task = db.query(TaskModel).get(task_id)
     if not one_task:
          raise HTTPException(404 , detail="Task ID is incorrect")
     return one_task
     # return{"status":"Task Fetched Successfully " , "data":one_task }

def update_task(body:Taskschema , task_id:int , db:Session):
     one_task = db.query(TaskModel).get(task_id)
     if not one_task:
          raise HTTPException(404 , detail="Task ID is incorrect")
    #  one_task.title = body.title
    #  one_task.description = body.description
    #  one_task.is_completed = body.is_completed

     body = body.model_dump()
     for field , value in body.items():
         setattr(one_task , field , value)

     db.add(one_task)
     db.commit()
     db.refresh(one_task)
     return one_task
     # return {"status":"Task Updated Successfully" , "data":one_task}


def delete_task(task_id:int , db:Session):
     one_task = db.query(TaskModel).get(task_id)
     if not one_task:
          raise HTTPException(404 , detail="Task ID is incorrect")
     
     db.delete(one_task)
     db.commit()
     
     return None