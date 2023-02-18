from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import status, Response, HTTPException

def get_all(db: Session):
    blogs= db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session, current_user: schemas.User):
    new_blog = models.Blog(title = request.title, body = request.body, user_id = current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot found the blog with same id..")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'success!!'

def update(id: int, request: schemas.BlogUpdate, db: Session):
    print(request)
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot found the blog with same id..")
    blog.update(request.dict(exclude_unset=True))
    db.commit()
    return 'success!!'

def show(id: int, response: Response, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {id} is not available')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f'Blog with the id {id} is not available'}
    return blog