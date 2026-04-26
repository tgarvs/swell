from fastapi import FastAPI
import routers.spots as rs
import routers.forecast as rf
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(rs.router)
app.include_router(rf.router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}