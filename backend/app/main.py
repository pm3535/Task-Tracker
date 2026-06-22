from fastapi import FastAPI
from app.api.routers import  auth_router, user_router,task_router


app = FastAPI()

app.include_router(auth_router.router)
app.include_router(user_router.router)
app.include_router(task_router.router)

@app.get('/')
async def task_tracker():
    return{'status': 'ok'}