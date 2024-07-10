from fastapi import FastAPI
import uvicorn

app = FastAPI(
        title="rafGPT",
        description="Portfolio: Rafael Alesso",
        version="1.0.0",
        debug=True
)

if __name__=="__main__":
    uvicorn.run("main:app", port=8000, reload=True)