from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schema
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/", response_model=List[schema.TeamsResponse])
def read_teams(db: Session = Depends(get_db)):
    return crud.get_teams(db)

@router.get("/{team_id}", response_model=schema.TeamsResponse)
def read_team(team_id: int, db: Session = Depends(get_db)):
    team = crud.get_team(db, team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Команда не найдена")
    return team

@router.post("/", response_model=schema.TeamsResponse)
def create_new_team(team: schema.TeamsCreate, db: Session = Depends(get_db)):
    return crud.create_team(db, team)

@router.put("/{team_id}", response_model=schema.TeamsResponse)
def update_team(team_id: int, team: schema.TeamsUpdate, db: Session = Depends(get_db)):
    update_team = crud.update_team(db, team_id, team)
    if not update_team:
        raise HTTPException(status_code=404, detail="Команда не найдена")
    return update_team

@router.delete("/{team_id}", response_model=schema.TeamsResponse)
def delete_team(team_id: int, db: Session = Depends(get_db)):
    delete_team = crud.delete_team(db, team_id)
    if not delete_team:
        raise HTTPException(status_code=404, detail="Команда не найдена")
    return delete_team