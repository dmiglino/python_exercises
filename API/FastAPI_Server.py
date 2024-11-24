from fastapi import FastAPI
import nest_asyncio
import uvicorn
import random

app = FastAPI()

max_value = 1000

@app.post("/set_max/{max}")
async def set_max(max: int):
    global max_value
    max_value = max
    return {"message": "Max value updated!", "max_value": max_value}

@app.get("/get_value")
async def get_value():
    num = random.randint(1, max_value)
    return num
    
if __name__ == "__main__":
    nest_asyncio.apply()
    uvicorn.run(app)

