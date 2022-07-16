from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import List, Union
from models import Role, User, Paper
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

dummydb = []

@app.get("/")
async def getAllPapers():
    return dummydb

@app.post("/papers", response_model=Paper)
async def addPapers(paper: Paper):
    dummydb.append(paper)
    return {"paper named {paper.title} is created: {paper}"}
    
@app.put("/papers/{paper_id}")
async def update_item(
    *,
    paper_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: Union[str, None] = None,
    paper: Union[Paper, None] = None,
):
    results = {"paper_id": paper_id}
    if q:
        results.update({"q": q})
    if paper:
        results.update({"paper": paper})
    return results