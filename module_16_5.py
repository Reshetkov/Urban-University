from fastapi import FastAPI, Path, Body, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Annotated, List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get(path="/user/{user_id}")
def get_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})

    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")



@app.post("/user/{username}/{age}")
def post_user(user: User):
    user.id = len(users) + 1
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: int, username: str, age: int):
    try:
        user = users[user_id - 1]
        user.username = username
        user.age = age
        users[user_id - 1] = user
        return user
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                i = user.id
        temp = users[i - 1]
        del users[i - 1]
        return temp

    except UnboundLocalError:
        raise HTTPException(status_code=404, detail="User was not found")

#    uvicorn module_16_5:app
