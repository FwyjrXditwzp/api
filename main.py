from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from services.fetcher import execute
from services.fetch_schdule import *
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://guacomolenigapenis.netlify.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/avg",description="зібрати статистику всіх челів + впорядковану") 
def call_allavg():
    return execute(f"call stud.GetStudentAverages()")

@app.get("/avg/{adr}",description="статистика по предметам одного студіка")
def call_fetcher(adr: int):
    return execute(f"call stud.GetOneStudentAverages({adr})")

@app.get("/rate",description="топ всіх студіків")
def call_allrate():
    return execute(f"call stud.GetTopRate()")

@app.get("/rate/{top}",description="топ до adr студіків")
def call_defrate(top: int):
    return execute(f"call stud.GetTopRateDef({top})")

@app.get("/avgmarks/",description="обща статка по предметам")
def call_avg_marks():
    return execute(f"call stud.GetAverageMarks()")

@app.get("/oddschedule/", description="розклад по чисельнику")
def fetch_odd_schedule():
    return schedule_odd 

@app.get("/evenschedule/", description="розклад по знаменнику")
def fetch_even_schedule():
    return schedule_even

@app.get("/schedule/", description="автоматичний розклад")
def fetch_schedule():
    return pick_schedule() 

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
