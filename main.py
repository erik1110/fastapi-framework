from typing import Optional
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/about')
def about():
    return {"data": "about page"}

@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published
    if published:
        return {"data": f"{limit} published blogs from db" }
    else:
        return {"data": f"{limit} blogs from db" }

@app.get('/blog/unmatch')
def unmatch():
    # you should push this function before show
    # cause fastapi sequentially find the route
    return {"data": "unmatch" }

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {"data": id }

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)