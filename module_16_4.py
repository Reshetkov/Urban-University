from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Annotated, List

app = FastAPI()
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
def get_users():
    return users


@app.post("/user/{username}/{age}")
def create_user(user: User):
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

#    uvicorn module_16_4:app
