from fastapi import FastAPI

app = FastAPI(
    title="AI Job Application API",
    version="1.0.0",
    description="API for AI-Based Job Application & Career Support System",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
