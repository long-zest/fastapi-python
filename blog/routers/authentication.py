from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, jwttoken
from sqlalchemy.orm import Session
from ..hashing import Hash
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Auth']
)

get_db = database.get_db

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Opps something wrong with your value...")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Opps something wrong with your value...")
    
    # Generate jwt token

    access_token = jwttoken.create_access_token(
        data={
            "sub": user.email,
            "id": user.id,
        }
    )
    return {"access_token": access_token, "token_type": "bearer"}