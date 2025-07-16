from fastapi import FastAPI
from . import crud, schemas

app = FastAPI()

@app.get('/api/reports/top-products')
def top_products(limit: int = 10):
    return crud.get_top_products(limit)

@app.get('/api/channels/{channel_name}/activity')
def channel_activity(channel_name: str):
    return crud.get_channel_activity(channel_name)

@app.get('/api/search/messages')
def search_messages(query: str):
    return crud.search_messages(query) 