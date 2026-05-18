import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from config.settings import settings       
from config.lifespan import app_lifespan  

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=app_lifespan,
    docs_url="/docs"
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "healthy", "project": settings.PROJECT_NAME}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)