import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {"data": {"hello world!": '123'}}

@app.get('/about')
def about():
    return {"data": "about page"}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)