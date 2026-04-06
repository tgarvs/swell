from fastapi import FastAPI
import routers.spots as rs
import routers.forecast as rf

app = FastAPI()
app.include_router(rs.router)
app.include_router(rf.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}