from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# Testing stuff...
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} blogs from the db'}
    else:
        return {'nothing here'}

@app.get('blog/unpublished')
def unPubListed():
    return {'some un-published here'}

@app.get('/blog/{id}')
def show(id):
    # some condition logic here
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # same like show
    return {'data': {'1', '2'}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(request: Blog):
    return request