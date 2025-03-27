from pydantic import BaseModel

class TeamsBase(BaseModel):
    name: str
    city: str
    sports: str
    founded_year: int | None = None
    championships: int |None = None
    
class TeamsCreate(TeamsBase):
    pass    

class TeamsUpdate(TeamsBase):
    pass

class TeamsResponse(TeamsBase):
    id: int
    
    class Config:
        orm_mode = True