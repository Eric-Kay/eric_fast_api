from fastapi import FastAPI , Response, status, HTTPException, Depends, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import  get_db
from app import schemas, models, utils, oauth


router = APIRouter()

@router.post("/login")
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= f" invalid credentials")
    

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code= status.HTTP_403_FORBIDDEN, detail= f" invalid credentials")
    

    access_token = oauth.create_access_token(data= {"user_id": user.id})
    

    return {"access_token": access_token, "token_type": "bearer"}




