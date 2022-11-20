from fastapi import FastAPI
from random import randint
import json

app = FastAPI()




@app.get("/back")
async def get_backexercise():
    #extract data from exercises.json for back exercises
    with open('exercises.json') as f:
        data = json.load(f)
    back = data['back']
    return back[str(randint(1, len(back)))]["name"]

@app.get("/chest")
async def get_chestexercise():
    #extract chest exercises from exercises.json and return the name of the first one
    with open('exercises.json') as f:
        data = json.load(f)
    chest = data['chest']
    return chest[str(randint(1, len(chest)))]["name"]
@app.post("/group/{group}")
async def make_group(group: str):
    #check if group is back or chest and return the corresponding exercise
    with open('exercises.json') as f:
        data = json.load(f)
    if group == 'back':
        back = data['back']
        return back
    elif group == 'chest':
        chest = data['chest']
        return chest
    else:
        return 'Invalid group'
    
    