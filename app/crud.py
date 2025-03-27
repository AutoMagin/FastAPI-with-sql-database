from sqlalchemy.orm import Session
from app import models, schema

def get_team(db: Session, team_id: int):
    return db.query(models.Team).filter(models.Team.id == team_id).first()

def get_teams(db: Session):
    return db.query(models.Team).all()

def create_team(db: Session, team: schema.TeamsCreate):
    db_team = models.Team(**team.dict())
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def update_team(db: Session, team_id : int, team_update: schema.TeamsUpdate):
    db_team = get_team(db, team_id)
    if db_team:
        for key, value in team_update.dict(exclude_unset=True).items():
            setattr(db_team, key, value)
        db.commit()
        db.refresh(db_team)
    return db_team


def delete_team(db: Session, team_id: int):
    db_team = get_team(db, team_id)
    if db_team:
        db.delete(db_team)
        db.commit()
    return db_team