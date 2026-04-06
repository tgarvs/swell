from fastapi import FastAPI
import routers.spots as rs

app = FastAPI()
app.include_router(rs.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}