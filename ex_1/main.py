from fastapi import FastAPI
from models import UserNumber


app = FastAPI()

@app.post("/minus")
async def minus(input : UserNumber):
    result = -input.number
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)