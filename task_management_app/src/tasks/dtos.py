from pydantic import BaseModel


class Taskschema(BaseModel):
     title :str
     description : str
     is_completed :bool = False