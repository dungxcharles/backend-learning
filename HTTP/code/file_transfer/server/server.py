from fastapi import FastAPI, File
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

@app.get("/")
def getFile():
    file = "confidential.txt"
    return FileResponse(file)

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=5000)