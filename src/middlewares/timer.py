# src/middlewares/timer.py
import time
from fastapi import Request

async def response_time_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    duration = time.time() - start_time
    response.headers["X-Process-Time"] = f"{duration:.4f} s"
    return response
