from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import recommendations

app = FastAPI(title="SlotForce AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recommendations.router, prefix="/api/v1/recommendations")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "SlotForce AI"}