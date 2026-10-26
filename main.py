from datetime import datetime
from fastapi import FastAPI, Request, Response
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time
import uvicorn

from .routers import items, jsonutils, smsutils, mdigitax


# 1. Setup daily rolling log handler
def setup_logging():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("fastapi_middleware_logger")
    logger.setLevel(logging.INFO)
    
    # Avoid duplicate logs if middleware re-initializes
    if not logger.handlers:
        handler = TimedRotatingFileHandler(
            "logs/app.log", when="midnight", interval=1, backupCount=30
        )
        handler.suffix = "%Y-%m-%d"
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname).3s] %(message)s"
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
    return logger

app = FastAPI(title="MApi Utils")
logger = setup_logging()

# 2. Add middleware to intercept all requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Process the request and get the response
    response = await call_next(request)
    
    # Calculate execution time
    process_time = (time.time() - start_time) * 1000
    
    # Log request details into the rolling file
    logger.info(
        f"Method: {request.method} | "
        f"Path: {request.url.path} | "
        f"Status: {response.status_code} | "
        f"Duration: {process_time:.2f}ms"
    )
    
    return response

# app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(jsonutils.router, prefix="/jutils", tags=["json-utils"])
app.include_router(smsutils.router, prefix="/smsutils", tags=["sms-utils"])
app.include_router(mdigitax.router, prefix="/digitax", tags=["digitax-utils"])

@app.get("/")
async def read_root():
     now = datetime.now()
     return {
         "status": "running", 
         "service": "FastAPI Service Simulator",
         "checkedat": now.isoformat()[:-3]
         }

# This block is critical for the service worker execution
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)
