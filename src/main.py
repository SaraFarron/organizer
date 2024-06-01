from fastapi import FastAPI

from src.charts.router import router as charts_router
from src.database import engine
from src.models import Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(charts_router, prefix="/auth", tags=["Auth"])
