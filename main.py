from fastapi import FastAPI
from fastapi.responses import FileResponse

from routers import meetups, organisers

app = FastAPI(title="PyData Global API")

app.include_router(organisers.router)
app.include_router(meetups.router)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def index():
    return FileResponse("static/index.html")
