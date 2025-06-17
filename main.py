from fastapi import FastAPI, Depends, HTTPException, Request
from app.model import predict_sentiment
from app.auth import verify_token
from app.schemas import TextInput
from app.rate_limit import limiter
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse
from slowapi.middleware import SlowAPIMiddleware
from app.utils import log_request

app = FastAPI()
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

@app.exception_handler(RateLimitExceeded)
def rate_limit_handler(request, exc):
    return JSONResponse(status_code=429, content={"error": "Too many requests!"})

@app.post("/predict")
@limiter.limit("5/minute")
def predict(request: Request, input: TextInput, token: str = Depends(verify_token)):
    user = token.get("user", "anonymous")
    log_request(user, input.text)
    sentiment = predict_sentiment(input.text)
    return {"sentiment": sentiment}
