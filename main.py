from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def task_tracker():
    return{'status': 'ok'}