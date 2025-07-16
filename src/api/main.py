from fastapi import FastAPI, HTTPException, Query
from . import crud, schemas
from typing import List

app = FastAPI(title="Telegram Medical Analytics API", description="Analytical endpoints for Telegram medical business data.")

@app.get('/api/reports/top-products', response_model=List[schemas.TopProduct])
def top_products(limit: int = Query(10, gt=0, le=100)):
    try:
        result = crud.get_top_products(limit)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/channels/{channel_name}/activity', response_model=schemas.ChannelActivity)
def channel_activity(channel_name: str):
    try:
        result = crud.get_channel_activity(channel_name)
        if not result:
            raise HTTPException(status_code=404, detail="Channel not found")
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/search/messages', response_model=List[schemas.Message])
def search_messages(query: str = Query(..., min_length=2)):
    try:
        result = crud.search_messages(query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 